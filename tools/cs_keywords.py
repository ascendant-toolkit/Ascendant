"""Extra key words for A Level Computer Science pages. build.py adds them to the end of each page's Learn tab.

"term | meaning". A leading * marks wider reading: a word that is not in the 9618 syllabus wording.
(14.1 has its own key words, built into the pages by artifact-kit/kw141.py.)
"""
import re

WORDS = {
    # 1 Information representation
    "ac-1-1-1-number-bases-bcd-hex": [
        "Most significant bit (MSB) | The leftmost bit, with the largest place value",
        "Least significant bit (LSB) | The rightmost bit, with the smallest place value"],
    "ac-1-1-2-negative-numbers-binary-arithmetic": [
        "*Sign and magnitude | A signed format in which the first bit gives the sign and the other bits give the size",
        "Underflow | A result too small to be represented in the space available"],
    "ac-1-1-3-character-sets": [
        "Character code | The binary number that represents one character in a character set",
        "*Code point | The number Unicode gives to a character",
        "*Control character | A code that performs an action, such as a new line, instead of showing a symbol"],
    "ac-1-2-1-bitmap-and-vector-graphics": [
        "*Metadata | Data describing a file, such as its width, height and colour depth in the file header",
        "*Pixel density | The number of pixels per inch (PPI) of a screen or image"],
    "ac-1-2-2-sound-sampling": [
        "ADC (analogue-to-digital converter) | Turns an analogue signal into digital values by sampling it",
        "DAC (digital-to-analogue converter) | Turns digital values back into an analogue signal, for example for a speaker",
        "*Bit rate | The number of bits used for each second of sound: sampling rate × sampling resolution × channels",
        "*Nyquist theorem | The sampling rate should be at least twice the highest frequency in the sound"],
    "ac-1-3-compression": [
        "Redundant data | Repeated or unnecessary data that compression can store more briefly or remove",
        "*Compression ratio | Original file size divided by compressed file size",
        "*Dictionary compression | Replaces repeated patterns with short codes that are looked up in a table",
        "*Huffman coding | Lossless coding that gives the most frequent symbols the shortest bit patterns",
        "*Perceptual coding | Lossy compression that removes detail people are unlikely to hear or see",
        "*MP3 | A lossy format for sound", "*JPEG | A lossy format for photographs", "*PNG | A lossless format for bitmap images"],
    # 2 Communication
    "as-2-1-1-networks-models-topologies": ["Subnetwork | A smaller section of a larger network"],
    "as-2-1-2-cloud-computing-transmission-media": [
        "*Attenuation | The weakening of a signal as it travels",
        "*Total internal reflection | How light stays inside a fibre-optic cable, reflecting off the boundary",
        "*Geostationary satellite | A satellite that stays above the same point on the Earth"],
    "as-2-1-3-lan-hardware-router-ethernet": ["*Gateway | A device that connects networks that use different protocols"],
    "as-2-1-4-internet-www-bit-streaming": ["*Progressive download | The file is downloaded to the device and can start playing before the download finishes"],
    "as-2-1-5-ip-addresses-urls-dns": [
        "Subnet mask | A pattern of bits showing which part of an IP address is the network ID and which is the host ID",
        "Resolve | To find the IP address that matches a domain name, which is the job of DNS",
        "*NAT (Network Address Translation) | Lets devices with private IP addresses share one public IP address",
        "*CIDR | Notation such as /24 giving the number of bits in the network ID"],
    # 3 Hardware
    "as-3-1-4-monitoring-control-sensors-feedback": [
        "Threshold (stored value) | The value a sensor reading is compared with to decide what to do",
        "Real-time system | A system that processes input quickly enough for its response to affect what is happening"],
    "as-3-2-1-logic-gates-circuits": ["Problem statement | A description in words of when an output should be 1, used to build the circuit, expression or truth table"],
    # 4 Processor fundamentals
    "as-4-1-2-performance-ports": [
        "Multi-core processor | A processor with more than one core, each able to fetch and execute instructions",
        "*Word length | The number of bits the processor handles in one operation",
        "*Overclocking | Running a processor faster than its rated clock speed, which produces more heat"],
    "as-4-1-3-fetch-execute-interrupts": [
        "Opcode | The part of an instruction that says which operation to carry out",
        "Operand | The data, or the address of the data, that the instruction works on",
        "*Interrupt vector table | A table holding the start address of the handling routine for each type of interrupt"],
    "as-4-2-1-assembly-language-assembler": [
        "*Directive | An instruction to the assembler itself, which produces no machine code instruction",
        "*Macro | A named block of instructions that the assembler copies in wherever the name is used"],
    "as-4-3-bit-manipulation": ["Monitoring and control using bits | Each bit of a register can stand for one sensor or device: AND with a mask tests it, OR sets it, XOR changes it"],
    # 5 System software
    "as-5-1-1-operating-system-management": ["Kernel | The central part of the operating system, which stays in memory and manages processes, memory and hardware"],
    "as-5-2-1-language-translators": [
        "*Bytecode | Intermediate code produced by partial compilation, such as Java's",
        "Virtual machine | Software that executes the intermediate code on a particular computer"],
    # 6 Security, privacy and integrity
    "as-6-1-1-security-privacy-integrity": ["Anti-spyware | Software that detects and removes programs that secretly record what a user does"],
    "as-6-1-2-security-threats": [
        "*Worm | Malware that copies itself across a network without needing a host file",
        "*Trojan horse | Malware disguised as useful software",
        "*Ransomware | Malware that locks or encrypts files and demands payment",
        "*Keylogger | Records keys pressed, for example to capture passwords",
        "*Adware | Software that shows unwanted adverts",
        "*Social engineering | Tricking people into giving away information or access",
        "*Denial of service | Flooding a server with requests so that real users cannot use it",
        "*Brute-force attack | Trying every possible password or key until one works",
        "*Two-factor authentication | Two different kinds of proof, such as a password and a code sent to a phone"],
    "as-6-2-1-data-validation": ["Modulo arithmetic | Using the remainder after division, for example to calculate a check digit"],
    "as-6-2-2-data-verification": ["*ARQ (Automatic Repeat Request) | The receiver acknowledges good data; data is sent again if there is an error or no acknowledgement in time"],
    # 7 Ethics and ownership
    "as-7-1-1-ethics-copyright-licences": [
        "*Plagiarism | Presenting someone else's work as your own", "*Software piracy | Copying or distributing software without permission"],
    "as-7-1-2-artificial-intelligence": [
        "Environmental impact | Effects on the planet, such as the energy and water used to train and run AI, or savings from using resources better",
        "*Autonomous system | A system that makes decisions and acts without direct human control",
        "*Machine learning | AI in which a system improves from data instead of following only fixed rules"],
    # 8 Databases
    "as-8-1-2-er-diagrams-normalisation": ["Link table | A table placed between two entities to replace a many-to-many relationship with two one-to-many relationships"],
    "as-8-2-database-management-systems": [
        "Data modelling | Showing the data and the relationships between data, for example in an E-R diagram",
        "Data security | Protecting data, for example with backups and access rights"],
    # 9 to 12 Algorithms, programming and development
    "as-9-1-abstraction-decomposition": ["*Pattern recognition | Spotting similarities between problems so that one solution can be reused"],
    "as-9-2-1-algorithms-flowcharts-identifiers": ["Structured English | A description of an algorithm in short English statements arranged by sequence, selection and iteration"],
    "as-9-2-2-stepwise-refinement": [
        "Logic statement | A condition that is TRUE or FALSE, used to define part of an algorithm", "Sub-task | A smaller part of a task",
        "*Top-down design | Starting with the whole problem and breaking it into smaller parts"],
    "as-10-1-data-types-records": ["FILE | The pseudocode data type for a file"],
    "as-10-2-1-arrays-processing": [
        "Lower bound | The first index of an array", "Upper bound | The last index of an array",
        "Linear data structure | Items arranged one after another, such as a 1D array",
        "Nested loop | A loop inside another loop, used to visit every element of a 2D array"],
    "as-10-4-abstract-data-types": ["Enqueue | Add an item to the rear of a queue", "Dequeue | Remove the item at the front of a queue"],
    "as-11-1-programming-basics": [
        "Input | Reading data, in pseudocode with INPUT", "Initialisation | Giving a variable its first value",
        "Logical operator | AND, OR and NOT, which combine or reverse conditions",
        "Concatenation | Joining strings end to end, with &amp; in pseudocode"],
    "as-11-3-structured-programming": [
        "Return value | The value a function sends back, which replaces the call in the expression",
        "Interface | The name, parameters and return type that show how a procedure or function is called"],
    "as-12-2-1-structure-charts": [
        "Decompose | To break a problem into sub-tasks", "*Data flow (data couple) | The arrow on a structure chart showing a parameter passed between modules"],
    "as-12-2-2-state-transition-diagrams": ["*Finite state machine | A system with a fixed number of states that moves between them in response to inputs"],
    "as-12-3-1-errors-and-testing": [
        "Test strategy | The overall approach to testing: what will be tested, how and when", "Debugging | Finding and correcting errors in a program"],
    "as-12-3-2-program-maintenance": [
        "Amendment | A change made to an existing program", "Enhancement | A change that adds to or improves what a program does",
        "*Preventive maintenance | Changes made to stop future problems"],
    # 13 Data representation
    "ac-13-1-1-non-composite-types": ["Dereferencing | Using a pointer to reach the data at the address it holds"],
    "ac-13-1-2-composite-types": ["Property (attribute) | A data item belonging to a class"],
    "ac-13-2-2-hashing": [
        "*Synonyms | Different record keys that hash to the same address", "*Load factor | The proportion of a hashed file that is in use"],
    "ac-13-3-1-floating-point-conversion": ["*Fixed-point | A format with the binary point always in the same position"],
    "ac-13-3-2-floating-point-accuracy": ["Accumulated error | Small rounding errors adding up over repeated calculations"],
    # 14.2 Switching
    "ac-14-2-2-packet-switching-routers": [
        "*Datagram | A packet sent on its own, which each router forwards independently",
        "*Connectionless | Data is sent without first setting up a path",
        "*Virtual circuit | A route agreed before sending, which all the packets then follow",
        "*Static routing | Routes are set by hand and stay the same",
        "*Dynamic routing | Routers update their routing tables as network conditions change"],
    # 15 Hardware and virtual machines
    "ac-15-1-1-risc-cisc-pipelining": [
        "*Microprogrammed control unit | Carries out each instruction as a series of smaller stored steps, typical of CISC",
        "*Pipeline flush | Discarding the partly processed instructions, for example after a jump or an interrupt",
        "*Data hazard (data dependency) | An instruction needs a result that an earlier instruction has not yet produced"],
    "ac-15-1-2-computer-architectures": [
        "*Multicomputer | Several computers, each with its own memory, working together by passing messages",
        "*Grid computing | Computers in different places sharing work on one large task"],
    "ac-15-1-3-virtual-machines": [
        "*Virtualisation | Creating a software version of hardware so that several systems can share one computer",
        "Sandbox | An isolated environment where software can run without affecting the host",
        "*Snapshot | A saved copy of a virtual machine's state that can be restored"],
    "ac-15-2-1-logic-circuits-adders": ["*Combinational circuit | A circuit whose output depends only on its current inputs, such as an adder"],
    "ac-15-2-2-flip-flops": [
        "*Bistable | Having two stable states, so it can store one bit",
        "*Synchronous | Changing only on a clock pulse"],
    "ac-15-2-4-karnaugh-maps": [
        "*Minterm | One product term that is 1 for exactly one row of the truth table",
        "*Don't care condition | An input combination that never occurs or does not matter, so it may be grouped as 0 or 1"],
    # 16 System software
    "ac-16-1-1-os-purposes-resources": [
        "I/O (input/output) | Transfer of data between the computer and its peripheral devices",
        "*Direct Memory Access (DMA) | A controller moves data between a device and memory without the processor handling each item",
        "*Bottleneck | The slowest part of a system, which limits overall speed",
        "*Spooling | Queuing output, such as print jobs, on disk so that the processor need not wait",
        "*Caching | Keeping often-used data in faster memory"],
    "ac-16-1-2-process-states-interrupts": [
        "*Process control block (PCB) | The data the operating system keeps about a process, such as its state and register contents",
        "*Context switch | Saving the state of one process and loading the state of another",
        "*High-level scheduler | Chooses which programs are admitted from backing store into memory",
        "*Volatile environment | The register contents that must be saved when a process is interrupted"],
    "ac-16-1-4-virtual-memory-paging-segmentation": [
        "Present flag | A bit in the page table showing whether the page is in main memory",
        "*Least frequently used (LFU) | A page replacement method that removes the page used the fewest times"],
    "ac-16-2-1-interpreters-compilation-stages": [
        "*Keyword table | The list of the language's reserved words and their tokens, used in lexical analysis",
        "*Semantic error | A statement that follows the grammar but does not make sense, such as adding a string to an integer",
        "*Error report | The list of errors the compiler produces, with their positions"],
    # 17 Security
    "ac-17-1-1-symmetric-asymmetric-encryption": [
        "*Session key | A symmetric key used for one communication session only",
        "*Brute-force attack | Trying every possible key until the message can be read"],
    "ac-17-1-2-quantum-cryptography": [
        "*Qubit | A quantum bit, which can be in a combination of 0 and 1 until it is measured",
        "*Superposition | Being in a combination of states at the same time",
        "*Entanglement | Linked particles whose measured states are related, even when far apart",
        "*Quantum key distribution (QKD) | Sharing an encryption key using photons, so that eavesdropping can be detected"],
    "ac-17-1-3-ssl-tls": ["*VoIP (Voice over IP) | Voice calls over the internet, which can be protected with TLS"],
    "ac-17-1-4-digital-certificates-signatures": ["*X.509 | The common standard format for digital certificates"],
    # 18 Artificial intelligence
    "ac-18-1-1-graphs-in-ai": ["Heuristic | An estimate, such as the straight-line distance to the goal, that guides a search"],
    "ac-18-1-2-dijkstra-a-star": [
        "h value (heuristic) | The estimated cost from a node to the goal",
        "*Admissible heuristic | One that never overestimates the true cost, so A* can find a shortest path",
        "*Predecessor | The previous node on the best path found so far, used to trace the route back"],
    "ac-18-1-3-machine-learning-categories": [
        "*Classification | Predicting which category an item belongs to",
        "*Penalty | A negative signal telling a reinforcement learning agent that an action was poor",
        "*Test data | Data kept back from training to check how well the model works",
        "*Overfitting | Learning the training data so closely that new data is predicted badly",
        "*Semi-supervised learning | Training with a little labelled data and a lot of unlabelled data"],
    "ac-18-1-4-neural-networks-backpropagation-regression": [
        "*Learning rate | How large a change is made to the weights at each step",
        "*Epoch | One pass through the whole set of training data",
        "*Threshold | The value a neuron's total input must reach for it to activate",
        "*Linear regression | Fitting a straight line to data to predict a numerical value"],
    # 19 and 20
    "searching-algorithms": ["Divide and conquer | Repeatedly splitting a problem into smaller parts, as a binary search halves the list"],
    "sorting-algorithms": ["*Stable sort | Items with equal keys stay in their original order"],
    "abstract-data-types": [
        "Dictionary | An ADT that stores key and value pairs and finds a value by its key",
        "*Heap (free list) | The store of unused nodes from which new nodes are taken"],
    "ac-20-1-2-oop-terminology-class-design": [
        "Data hiding | Keeping attributes private so that outside code must use the class's methods",
        "*Overloading | Several methods with the same name but different parameters"],
    "ac-20-1-4-declarative-programming": [
        "Instantiation | Giving a variable a value while a goal is being satisfied",
        "*Unification | Matching a goal with a fact or rule head so that variables take values",
        "*Backtracking | Going back to try another match when a goal fails, or to find further answers",
        "*Anonymous variable | The underscore, used where the value does not matter"],
    "ac-20-2-1-file-processing": ["*Binary file | A file storing data in internal binary form; Python's pickle module can read and write records this way"],
    "ac-20-2-2-exception-handling": ["Robust program | One that copes with unexpected input or events without crashing"],
    # extra pages for sections 19 and 20
    "linked-lists": ["*Unordered linked list | A list whose items are not kept in any order, so a new item can be added at the start"],
    "insertion-sort": ["*Stable sort | Items with equal keys stay in their original order, as they do in an insertion sort"],
    "recursion-fibonacci": ["Recursive call | The line where a function calls itself"],
    "recursion-binary-tree": [
        "General case | The case in which the procedure calls itself again on a smaller part of the problem",
        "*Backtracking | Returning to a node after finishing one of its subtrees, as the calls unwind"],
    "recursion-binary-search": ["Divide and conquer | Repeatedly splitting a problem into smaller parts, as each call searches half of the list"],
    "recursion-lists-strings": [
        "Concatenation | Joining strings end to end", "Iteration | Repeating steps with a loop, the alternative to recursion"],
    "ac-20-1-3-oop-in-python": [
        "Instance | An object created from a class", "Property (attribute) | A data item belonging to a class",
        "Class diagram | A diagram showing a class's name, attributes and methods"],
    "ac-20-1-2-constructor": ["Instantiation | Creating an object from a class, which runs the constructor"],
    "ac-20-1-2-encapsulation": ["Data integrity | Data staying accurate and valid, which a setter can protect by checking new values"],
    "ac-20-1-2-getters-and-setters": ["*Accessor | Another name for a getter", "*Mutator | Another name for a setter"],
    "ac-20-1-2-inheritance": ["Base class | Another name for a parent class or superclass"],
    "ac-20-1-2-polymorphism": [
        "*Overloading | Several methods with the same name but different parameters. This differs from overriding",
        "*Dynamic binding | The choice of which method to run is made while the program is running, from the object's class"],
    "ac-20-1-2-containment": ["*Composition | A strong form of containment in which the parts do not exist without the whole"],
    "ac-20-2-1-storing-records-serial-sequential": ["Binary file | A file storing data in internal binary form, such as records written with Python's pickle module", "*pickle | The Python module that writes objects to a binary file and reads them back"],
    "ac-20-2-1-adding-to-random-file": ["Binary file | A file storing data in internal binary form, such as records written with Python's pickle module"],
    "ac-20-2-1-finding-in-random-file": ["Record key | The field that identifies a record and is used to work out its address", "Binary file | A file storing data in internal binary form, such as records written with Python's pickle module"],
    "ac-20-2-2-what-is-an-exception": ["Exception handler | The code that runs when an exception occurs"],
    "ac-20-2-2-why-and-when-exception-handling": ["Robust program | One that copes with unexpected input or events without crashing"],
    "ac-20-2-2-try-except-python": ["IndexError | Raised in Python when a list or string index is out of range"],
    "ac-20-2-2-exception-handling-files": [
        "with open | A Python statement that closes the file automatically, even if an exception occurs",
        "PermissionError | Raised when the program is not allowed to open the file",
        "*pickle | The Python module that writes objects to a binary file and reads them back",
        "*Corrupt file | A file whose contents are damaged or not in the expected form"],
}

START, END = "<!-- key words -->", "<!-- /key words -->"


def _table(rows):
    return ('<div class="tw"><table class="t"><tr><th>Key word</th><th>Meaning</th></tr>'
            + "".join(f"<tr><td><b>{w}</b></td><td>{m}</td></tr>" for w, m in rows) + "</table></div>")


def apply(page, slug):
    """Add the page's key words to the end of its Learn tab."""
    if slug not in WORDS or START in page:
        return page
    depth = 0
    for tag in re.finditer(r"<(/?)section\b", page[page.index('<section id="learn"'):]):   # the tab may hold sub-sections
        depth += -1 if tag[1] else 1
        if depth == 0:
            end = page.index('<section id="learn"') + tag.start()
            break
    pairs = [[x.strip() for x in w.split(" | ", 1)] for w in WORDS[slug]]
    core = [(w, m) for w, m in pairs if not w.startswith("*")]
    wider = [(w.lstrip("*"), m) for w, m in pairs if w.startswith("*")]
    block = START + '<div class="kit"><h2>More key words</h2>'
    if core:
        block += _table(core)
    if wider:
        block += ('<h3>Wider words</h3><p>Not in the 9618 syllabus wording. They help you understand the topic and read around it.</p>' + _table(wider))
    return page[:end] + block + "</div>\n" + END + "\n" + page[end:]
