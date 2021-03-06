#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import cover
import shutil
import traceback

def search_python_posix():
    lst = []
    path = os.environ.get("PATH")
    for item in path.split(":"):
        try:
            for interp in os.listdir(item):
                if interp[:6] != "python":
                    continue
                if interp[-7:] == "-config":
                    continue
                fp = os.path.join(item, interp)
                # test if already in list
                same = False
                for lidx, l_interp in enumerate(lst):
                    if os.path.samefile(l_interp, fp):
                        same = True
                        # use shorter name
                        if len(l_interp) < len(fp):
                            lst[lidx] = fp
                        break
                if same:
                    continue
                lst.append(fp)
        except OSError:
            pass
    return lst

def search_python_win():
    lst = []
    try:
        try:
            import _winreg as winreg
        except ImportError:
            import winreg
        def findreg(key, lst):
            PATH = "SOFTWARE\\Python\\PythonCore"
            try:
                rl = winreg.OpenKey(key, PATH)
            except WindowsError:
                return lst
            try:
                for i in range(winreg.QueryInfoKey(rl)[0]):
                    ver = winreg.EnumKey(rl, i)
                    rv = winreg.QueryValue(key, PATH + "\\" + ver + "\\InstallPath")
                    fp = os.path.join(rv, "python.exe")
                    #print fp
                    if os.path.exists(fp) and not fp in lst:
                        lst.append(fp)
            except WindowsError:
                pass
            return lst
        lst = findreg(winreg.HKEY_LOCAL_MACHINE, lst)
        lst = findreg(winreg.HKEY_CURRENT_USER, lst)
    except:
        traceback.print_exc()
        # fallback
        cover.log("Search python at system drive")
        try:
            path = os.environ.get("SystemDrive", "C:")
            for item in os.listdir(path):
                if item[:6].lower() != "python":
                    continue
                fp = os.path.join(path, item, "python.exe")
                if os.path.exists(fp) and not fp in lst:
                    lst.append(fp)
        except:
            traceback.print_exc()

    return lst

def search_python():
    if sys.platform.startswith("linux"):
        lst = search_python_posix()
    elif sys.platform.startswith("win"):
        lst = search_python_win()
    else:
        lst = search_python_posix()
    if len(lst) == 0:
        # fallback
        lst.append(sys.executable)
    return lst

def find_python_version(pylst):
    lst = []
    ids = []
    for interp in pylst:
        try:
            std, err = cover.exec_cmd([interp, "-V"])
            version = err.strip()
            if not version:
                # python 3.4+
                version = std.strip()
            if version[:6] == "Python":
                shver = version[6:].strip().replace(" ", "-")
                nid = shver
                nidn = 0
                while nid in ids:
                    nidn += 1
                    nid = shver + "-%d" % nidn
                ids.append(nid)
                lst.append((interp, nid, version))
            else:
                cover.err("Not a python", version)
                # no python found
                continue
        except:
            traceback.print_exc()
    return lst

def search_tests():
    base = os.path.join(cover.basepath, "cover")
    lst = []
    for item in os.listdir(base):
        if item[:5] != "test_" or item[-3:] != ".py":
            continue
        lst.append(os.path.join(base, item))
    lst.sort()
    return lst

def do_test_one(testfile, interp, info, dest):
    path = interp[0]
    nid = interp[1]
    destpath = dest[0]
    destenv = dest[1]
    # check PIL
    if info.get("pil", "no") == "yes":
        if destenv.get("pil", "no") != "yes":
            return ("skip", "no PIL or PIllow found")
    # check python version
    tool2to3 = (info.get("2to3", "no") == "yes")
    py2 = (info.get("python2", "yes") == "yes")
    py3 = (info.get("python3", "yes") == "yes")
    plat = info.get("platform", "*")
    if plat == "":
        plat = "*"
    if plat != "*":
        plats = plat.split(",")
        accept = False
        for plat in plats:
            if sys.platform == plat:
                accept = True
                break
        if not accept:
            return ("skip", "not for \"" + sys.platform + "\"")
    copy = False
    if nid[:2] == "3.":
        if not py3:
            return ("skip", "not for python 3")
        if not tool2to3:
            copy = True
        else:
            return ("unimplemented", "todo")
    if nid[:2] == "2.":
        if not py2:
            return ("skip", "not for python 2")
        copy = True

    # check if fpdf instaled
    if destenv.get("ver", "None") == "None":
        return ("nofpdf", "")

    # copy files
    testname = os.path.basename(testfile)
    testfmt = info.get("format", "raw")
    newfile = os.path.join(destpath, testname)
    newres = os.path.join(destpath, info.get("fn", testname + "." + testfmt.lower()))
    if copy:
        shutil.copy(testfile, destpath)
    # start execution
    std, err = cover.exec_cmd([path, "-B", newfile, "--check", "--auto", newres])
    f = open(os.path.join(destpath, "testlog.txt"), "a")
    f.write("#" * 40 + "\n")
    f.write(testname + "\n")
    f.write("=" * 40 + "\n")
    f.write(std)
    f.write("-" * 40 + "\n")
    f.write(err)
    f.close()

    answ = std.strip()
    if answ.find("\n") >= 0 or len(answ) == 0:
        return ("fail", "bad output")
    else:
        if answ == "HASHERROR":
            # get new hash
            nh = ""
            for line in err.split("\n"):
                line = line.strip()
                if line[:5] == "new =":
                    nh = line[5:].strip()
            return ("hasherror", nh)
        return (answ.lower(), "")


def prepare_dest(interp):
    destpath = os.path.join(cover.basepath, "out-" + interp[1])
    if not os.path.exists(destpath):
        os.makedirs(destpath)
    # copy common set
    src = os.path.join(cover.basepath, "cover")
    shutil.copy(os.path.join(src, "common.py"), destpath)
    shutil.copy(os.path.join(src, "checkenv.py"), destpath)
    f = open(os.path.join(destpath, "testlog.txt"), "w")
    f.write("Version: " + interp[1] + "\n")
    f.write("Path: " + interp[0] + "\n")
    f.write(str(interp[2:]) + "\n")

    # run checkenv
    std, err = cover.exec_cmd([interp[0], "-B", os.path.join(destpath, "checkenv.py")])
    env = {}
    if len(err.strip()) == 0:
        # OK
        f.write("Check environment - ok:\n")
        f.write(std)
        lineno = 0
        for line in std.split("\n"):
            lineno += 1
            line = line.strip()
            if lineno == 1:
                if line != "CHECK":
                    break
            line = line.strip()
            kv = line.split("=", 1)
            if len(kv) == 2:
                env[kv[0].lower().strip()] = kv[1].strip()
    else:
        f.write("ERROR:\n")
        f.write(err)
    f.close()
    return (destpath, env)

def do_test(testfile, interps, dests, stats, hint = ""):
    cover.log("Test", hint, ":", os.path.basename(testfile))
    info = cover.read_cover_info(testfile)
    resall = ""
    # prepare
    # do tests
    hasherr = []
    for interp in interps:
        if len(interps) < 6:
            resall += (interp[1] + " - ")
        res, desc = do_test_one(testfile, interp, info, dests[interp[1]])
        if res == "hasherror":
            hasherr.append(desc)
            #cover.log("HASH =", desc)
        # update statistic
        stats["_"]["_"] += 1
        stats["_"][res] = stats["_"].get(res, 0) + 1
        stats[interp[1]]["_"] += 1
        stats[interp[1]][res] = stats[interp[1]].get(res, 0) + 1
        resall += (res + " " * 10)[:6].upper()
        resall += "  "
    cover.log(resall)
    # test if all hash
    if len(interps) == len(hasherr):
        cover.err("All hashes wrong")

def print_interps(interps):
    cover.log(">> Interpretors:", len(interps))
    dests = {}
    stats = {"_": {"_": 0}}
    for idx, interp in enumerate(interps):
        cover.log("%d) %s - %s" % (idx + 1, interp[1], interp[0]))
    cover.log()

def do_all_test(interps, tests):
    print_interps(interps)
    dests = {}
    stats = {"_": {"_": 0}}
    for idx, interp in enumerate(interps):
        dests[interp[1]] = prepare_dest(interp)
        stats[interp[1]] = {"_": 0}

    cover.log(">> Tests:", len(tests))
    for idx, test in enumerate(tests):
        do_test(test, interps, dests, stats, "%d / %d" % (idx + 1, len(tests)))
    cover.log()

    cover.log(">> Statistics:")
    def stat_str(stat):
        keys = list(stat.keys())
        keys.sort()
        st = "total - %d" % stat["_"]
        for key in keys:
            if key == "_":
                continue
            st += (", %s - %d" % (key, stat[key]))

        return st
    for interp in interps:
        cover.log(interp[1] + ":", stat_str(stats[interp[1]]))
    cover.log("-"*10)
    cover.log("All:", stat_str(stats["_"]))

    # check if no FPDF at all
    total = stats["_"]["_"]
    fpdf = stats["_"].get("nofpdf", 0)
    skip = stats["_"].get("skip", 0)
    if skip == total:
        cover.log("All tests skipped. Install some modules (PIL, PyBIDI, Gluon etc)")
    elif fpdf + skip == total:
        hint_prepare()


def list_tests():
    tst = search_tests()
    cover.log(">> Tests:", len(tst))
    for idx, test in enumerate(tst):
        test = os.path.basename(test)
        if test[:5].lower() == "test_":
            test = test[5:]
        if test[-3:].lower() == ".py":
            test = test[:-3]
        cover.log("%d) %s" % (idx + 1, test))
    cover.log()

def usage():
    cover.log("Usage: runtest.py [...]")
    cover.log("  --listtests      - list all tests")
    cover.log("  --listinterps    - list all availiable interpretors")
    cover.log("  --test issuexx   - add test issuexx")
    cover.log("  --test @file     - add test from file")
    cover.log("  --interp path    - test against specified interpretors")
    cover.log("  --interp @file   - read interpretors list from file")
    cover.log("  --downloadfonts  - download font set")
    cover.log("  --help           - this page")


def hint_prepare():
    if cover.PYFPDFTESTLOCAL:
        if sys.platform.startswith("win"):
            prefix = ""
            suffix = ".bat"
        else:
            prefix = "./"
            suffix = ".sh"
        cover.log("*** Please, prepare local copy for tests")
        cover.log("***   " + prefix + "prepare_local" + suffix)
    else:
        cover.log("*** Please, install PyFPDF with")
        cover.log("***   python setup.py install")
        cover.log("*** or set PYFPDFTESTLOCAL variable to use local copy")
        if sys.platform.startswith("win"):
            cover.log("***   set PYFPDFTESTLOCAL=1")
        else:
            cover.log("***   export PYFPDFTESTLOCAL=1")


def read_list(fn):
    f = open(fn, "r")
    try:
        return f.readlines()
    finally:
        f.close()

def hasher(path, args):
    tags = []
    while len(args):
        arg = args[0]
        args = args[1:]
        if arg == "--tag":
            if len(args) == 0:
                cover.log("Param without value")
                return
            value = args[0]
            args = args[1:]
            if value not in tags:
                tags.append(value)
        else:
            cover.log("Unknown param")
            return

    lst = []
    if os.path.isdir(path):
        files = [(x.lower(), x) for x in os.listdir(path)]
        files.sort()
        for s, item in files:
            fp = os.path.join(path, item)
            # clear path
            bp = fp
            if sys.platform.startswith("win"):
                bp = fp.replace("\\", "/")
            lst += [[bp, cover.file_hash(fp)]]
    else:
        lst = [[path, cover.file_hash(path)]]
    for item, hs in lst:
        cover.log("res=" + item)
        cover.log("hash=" + hs)
        cover.log("tags=" + ",".join(tags))
        cover.log()

def download_fonts():
    URL = "http://pyfpdf.googlecode.com/files/fpdf_unicode_font_pack.zip"
    fntdir = os.path.join(cover.basepath, "font")
    zippath = os.path.join(cover.basepath, URL.split('/')[-1])
    if not os.path.exists(fntdir):
        os.makedirs(fntdir)
    if not os.path.exists(zippath):
        import urllib2
        u = urllib2.urlopen(URL)
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        cover.log("Downloading:", file_size, "bytes")
        f = open(zippath, "wb")
        file_size_dl = 0
        while True:
            buff = u.read(64 * 1024)
            if not buff:
                break
            file_size_dl += len(buff)
            f.write(buff)
            cover.log("  ", file_size_dl * 100. / file_size, "%")
        f.close()
    # unpack
    cover.log("Extracting")
    import zipfile
    fh = open(zippath, "rb")
    z = zipfile.ZipFile(fh)
    for name in z.namelist():
        if name[:5] != "font/":
            continue
        if name[5:].find("/") >= 0:
            continue
        cover.log("  ", name[5:])
        outfile = open(os.path.join(fntdir, name[5:]), "wb")
        outfile.write(z.read(name))
        outfile.close()
    cover.log("Done")

def main():
    cover.log("Test PyFPDF")

    testsn = []
    interpsn = []
    args = sys.argv[1:]
    while len(args):
        arg = args[0]
        args = args[1:]
        if arg == "--hash":
            if len(args) == 0:
                cover.log("Param without value")
                return usage()
            return hasher(args[0], args[1:])
        if arg == "--help":
            return usage()
        elif arg == "--test":
            if len(args) > 0:
                value = args[0]
                args = args[1:]
            else:
                cover.log("Param without value")
                return usage()
            if value[:1] == "@":
                # from file
                testsn += read_list(value[1:])
            else:
                testsn.append(value)
        elif arg == "--interp":
            if len(args) > 0:
                value = args[0]
                args = args[1:]
            else:
                cover.log("Param without value")
                return usage()
            if value[:1] == "@":
                # from file
                interpsn += read_list(value[1:])
            else:
                interpsn.append(value)
        elif arg == "--listtests":
            return list_tests()
        elif arg == "--listinterps":
            return print_interps(find_python_version(search_python()))
        elif arg == "--downloadfonts":
            return download_fonts()
        else:
            cover.log("Unknown param")
            return usage()

    if len(testsn) == 0:
        tests = search_tests()
    else:
        # cheack all tests
        tests = []
        for test in testsn:
            test = test.strip()
            fn = os.path.join(cover.basepath, "cover", "test_" + test + ".py")
            if os.path.exists(fn):
                tests.append(fn)
            else:
                cover.err("Test \"%s\" not found" % test)
                return

    if len(interpsn) == 0:
        interps = find_python_version(search_python())
    else:
        # cheack all tests
        interps = []
        for interp in interpsn:
            fn = os.path.abspath(interp)
            if os.path.exists(fn):
                interps.append(fn)
            else:
                cover.err("Interpretor \"%s\" not found" % test)
                return
        interps = find_python_version(interps)

    do_all_test(interps, tests)


if __name__ == "__main__":
    main()
