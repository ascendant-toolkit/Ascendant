"""Builds the IGCSE CS chapter 4 review artifacts from tools/artifact-kit/ch4/<id>.{learn.html,explore.html,js}.
Usage: python3 tools/artifact-kit/mk_ch4.py [id ...]   (no ids = all). Then python3 build.py from the repo root."""
import sys, pathlib, subprocess
d = pathlib.Path(__file__).parent; src = d / "ch4"
PARTS = {
    "c411": ("4.1.1", "System Software and Application Software", "ig-cs-system-application-software", "Operating systems, utilities and drivers against the apps you use: what each does, and the utilities that keep a computer healthy."),
    "c412": ("4.1.2", "Operating Systems", "ig-cs-operating-systems", "The functions of an operating system: interface, memory, security, hardware, files, multitasking and user accounts."),
    "c413": ("4.1.3", "Running of Applications", "ig-cs-running-applications", "How a computer starts up and how hardware, firmware (the BIOS) and the operating system work together to run an application."),
    "c414": ("4.1.4", "Interrupts", "ig-cs-interrupts", "Signals that make the processor pause, how they are serviced, and how buffers and interrupts keep printing and streaming smooth."),
    "c421": ("4.2.1", "High-Level and Low-Level Languages", "ig-cs-high-low-level-languages", "What separates a language written for people from one written for a machine, and the trade-offs of each."),
    "c422": ("4.2.2", "Assembly Languages", "ig-cs-assembly-languages", "Mnemonics, the accumulator, and why a few programmers still write assembly."),
    "c423": ("4.2.3", "Translators", "ig-cs-translators", "Compilers, interpreters and assemblers: what each translates, and what each produces."),
    "c424": ("4.2.4", "Compilers and Interpreters Compared", "ig-cs-compilers-interpreters", "The advantages and disadvantages of compiling and interpreting, and when each is the right choice."),
    "c425": ("4.2.5", "Integrated Development Environments", "ig-cs-ide", "The tools an IDE bundles for writing, running and debugging programs."),
}
common = (src / "common.js").read_text(); skel = (src / "skeleton.html").read_text()
for k in (sys.argv[1:] or PARTS):
    sec, title, slug, lead = PARTS[k]
    body = skel.replace("@@SEC@@", sec).replace("@@TITLE@@", title).replace("@@LEAD@@", lead)
    body = body.replace("@@LEARN@@", (src / f"{k}.learn.html").read_text()).replace("@@EXPLORE@@", (src / f"{k}.explore.html").read_text())
    (d / f"{k}.body.html").write_text(body); (d / f"{k}.js").write_text(common + "\n" + (src / f"{k}.js").read_text())
    subprocess.run([sys.executable, str(d / "assemble.py"), k, title, slug], check=True)
