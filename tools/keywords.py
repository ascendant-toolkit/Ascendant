"""Extra key words for lesson pages in every course. build.py adds them to the end of each page's Learn tab.

"term | meaning". A leading * marks wider reading: a word that goes beyond the main syllabus wording.
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
    # ---------------- IGCSE Computer Science
    "number-systems": [
        "Logic gate | A circuit that takes binary inputs and gives a binary output. Computers process data with logic gates",
    ],
    "igcse-compression-lab": [
        "Nibble | 4 bits",
        "Kibibyte (KiB) | 1024 bytes",
        "Mebibyte (MiB) | 1024 KiB",
        "Gibibyte (GiB) | 1024 MiB",
        "Tebibyte (TiB) | 1024 GiB",
        "Pebibyte (PiB) | 1024 TiB",
        "Exbibyte (EiB) | 1024 PiB",
        "Storage space | The room a file takes up on a storage device, which compression reduces",
        "Transmission time | How long a file takes to send, which is shorter for a smaller file",
    ],
    "ig-cs-data-transmission": [
        "Packet number | The number in a packet header used to put the packets back in order",
        "Originator's address | The address of the sending device, held in the packet header",
    ],
    "ig-cs-error-detection": [
        "Data loss | Bits go missing during transmission",
        "Data gain | Extra bits appear during transmission",
    ],
    "ig-cs-computer-architecture": [
        "*Overclocking | Running a CPU faster than its rated clock speed, which produces more heat",
    ],
    "ig-cs-network-hardware": [
        "*Switch | Connects devices on a local network and sends data only to the intended one",
        "*Wireless access point (WAP) | Lets wireless devices join a wired network",
        "*DHCP | The service that gives devices a dynamic IP address",
    ],
    "ig-cs-interrupts": [
        "Software interrupt | An interrupt caused by a program, such as division by zero or two processes using the same memory location",
        "Hardware interrupt | An interrupt caused by a device, such as a key press or a mouse movement",
        "*Interrupt queue | Interrupts waiting to be handled, in order of priority",
    ],
    "ig-cs-high-low-level-languages": [
        "Syntax | The rules for how statements must be written in a language",
    ],
    "ig-cs-assembly-languages": [
        "*Opcode | The part of an instruction giving the operation",
        "*Operand | The data or address the instruction uses",
    ],
    "ig-cs-ide": [
        "*Syntax highlighting | The code editor colours different parts of the code, which makes errors easier to spot",
    ],
    "internet-and-www": [
        "Favourite (bookmark) | A saved web address that can be opened again quickly",
        "Navigation tools | Browser buttons such as back, forward and refresh",
        "*ISP (internet service provider) | A company that provides access to the internet",
    ],
    "blockchain-explained": [
        "Digital currency | A currency that exists only electronically",
    ],
    "cyber-security": [
        "Secure Socket Layer (SSL) | A security protocol that encrypts data sent between a browser and a web server",
    ],
    "ig-cs-robotics": [
        "*End effector | The tool or gripper at the end of a robot arm",
        "*Autonomous robot | A robot that acts without a person controlling it",
    ],
    "ig-cs-artificial-intelligence": [
        "*Chatbot | A program that holds a conversation with a user",
        "*Neural network | Layers of linked nodes that learn patterns from data",
    ],
    "ig-cs-test-data": [
        "*Erroneous data | Another name for abnormal data, which should be rejected",
    ],
    "ig-cs-trace-tables-errors-algorithms": [
        "Syntax error | Code that breaks the rules of the language",
        "Logic error | The program runs but gives the wrong result",
        "Run-time error | An error while the program runs that stops it, such as division by zero",
    ],
    "ig-cs-file-handling": [
        "*Append | Adding data to the end of an existing file",
    ],
    "ig-cs-sql": [
        "*Wildcard (*) | In SELECT *, a symbol meaning all fields",
    ],
    # ---------------- IGCSE Economics
    "ig-allocation-questions": [
        "For whom to produce | The basic economic question of who receives the goods and services",
    ],
    "ig-factors-quantity-quality": [
        "*Human capital | The skills, knowledge and health of workers",
    ],
    "ig-ppc-points": [
        "Attainable point | A combination of goods on or inside the PPC, which can be produced with current resources",
    ],
    "ig-ppc-shifts": [
        "*Productive potential | The most an economy can produce with its resources and technology",
    ],
    "ig-how-markets-work": [
        "*Product market | A market where goods and services are bought and sold, unlike a factor market",
    ],
    "ig-demand-definition": [
        "Demand schedule | A table showing the quantity demanded at each price",
    ],
    "ig-supply-definition": [
        "Supply schedule | A table showing the quantity supplied at each price",
    ],
    "ig-supply-shifts": [
        "*Joint supply | Producing one good also produces another, such as beef and leather",
    ],
    "ig-pes-determinants": [
        "*Barriers to entry | Obstacles that stop new firms joining a market, which can make supply less elastic",
    ],
    "ig-mixed-system": [
        "*Planning | The government deciding how some resources are used",
    ],
    "ig-government-intervention": [
        "*Government failure | Government intervention that makes the use of resources worse",
        "*Specific tax | An indirect tax of a fixed amount on each unit",
        "*Ad valorem tax | An indirect tax charged as a percentage of the price",
    ],
    "ig-money": [
        "Recognisable | A characteristic of money: people can easily identify it as genuine",
    ],
    "ig-banking": [
        "*Shareholder | A part-owner of a company such as a commercial bank",
    ],
    "ig-wage-determination": [
        "*Derived demand | Demand for workers that comes from the demand for what they produce",
        "*Earnings | Total pay, including wages, overtime and bonuses",
    ],
    "ig-mergers": [
        "*Takeover | One firm gaining control of another, usually by buying most of its shares",
    ],
    "ig-fiscal-taxation": [
        "*Tax avoidance | Legally arranging affairs to pay less tax",
    ],
    "ig-supply-side-definition": [
        "*Productive potential | The most an economy can produce with its resources and technology",
    ],
    "ig-unemployment-types": [
        "*Voluntary unemployment | People choosing not to take jobs available at current wages",
    ],
    "ig-living-standards-indicators": [
        "*Per capita | Per person: the same meaning as per head",
    ],
    "ig-poverty-policies": [
        "*Aid | Help such as money, goods or expertise given to a country or group",
    ],
    "ig-population-factors": [
        "*Fertility rate | The average number of children born to each woman",
    ],
    "ig-population-effects": [
        "*Dependants | People, mainly children and older people, who rely on the income of those working",
    ],
    "ig-development-differences": [
        "*Debt | Money owed, whose repayments can reduce what a country has to spend on development",
    ],
    "ig-globalisation-definition": [
        "*Trade bloc | A group of countries that agree to reduce trade barriers between themselves",
    ],
    "ig-fx-determination": [
        "*Managed exchange rate | A rate set mainly by the market, with the central bank stepping in at times",
    ],
    "ig-fx-consequences": [
        "Export price | The price of a country's goods to foreign buyers, which changes when the exchange rate changes",
    ],
    "ig-bop-structure": [
        "*Credit | An item that brings money into a country, recorded as positive",
        "*Debit | An item that takes money out of a country, recorded as negative",
    ],
    # ---------------- AS and A Level Economics
    "as-market-economy": [
        "*Invisible hand | Adam Smith's idea that people acting in their own interest are guided by prices towards outcomes that benefit others",
    ],
    "as-merit-demerit-goods": [
        "Imperfect information | Consumers or producers lack full or accurate knowledge, so a good may be under- or over-consumed",
    ],
    "as-elasticity-of-supply": [
        "Factor mobility | How easily factors of production can move into producing a good, which raises PES",
    ],
    "as-related-markets": [
        "*Competitive supply | The same resources could make either good, so producing more of one means less of the other",
        "*Composite demand | A good demanded for several different uses",
    ],
    "as-reasons-for-intervention": [
        "Non-provision of public goods | A free market may not supply a public good at all, because of the free rider problem",
    ],
    "as-government-intervention": [
        "*Government failure | Government intervention that leads to a worse allocation of resources",
    ],
    "as-market-basic-prices-gross-net": [
        "Indirect taxes (in national income) | Subtracted, and subsidies added, to change a value at market prices into basic prices",
    ],
    "as-causes-consequences-of-growth": [
        "Externalities of growth | Effects of growth on third parties, such as pollution, which may not appear in GDP",
    ],
    "as-consequences-of-inflation": [
        "*Fiscal drag | Rising money incomes pull people into higher tax bands when the bands are not raised with inflation",
    ],
    "as-taxation": [
        "*Canons of taxation | Principles of a good tax, such as equity, certainty, convenience and economy",
    ],
    "as-protectionism-tools": [
        "*Exchange control | A government limit on buying foreign currency, which restricts imports",
    ],
    "as-exchange-rate-determination": [
        "Capital (financial) flows | Money moving between countries to invest or save, which changes demand for and supply of a currency",
    ],
    "as-correcting-current-account-imbalances": [
        "Monetary policy | Using interest rates, the money supply and credit rules; tighter policy may reduce spending on imports, and may also change the exchange rate",
    ],
    "private-external-costs-benefits": [
        "Moral hazard | A person takes more risk because someone else bears some of the cost, for example after buying insurance",
        "*Adverse selection | Hidden information before a deal means higher-risk people are more likely to take it",
    ],
    "cost-benefit-analysis": [
        "*Shadow price | An estimated value for a cost or benefit that has no market price",
    ],
    "short-run-production-and-costs": [
        "Law of variable proportions | Another name for the law of diminishing returns",
    ],
    "market-spectrum-perfect-competition": [
        "Barriers to exit | Obstacles that make it costly for a firm to leave a market, such as sunk costs",
    ],
    "why-and-how-firms-grow": [
        "*Synergy | A merged firm performing better than the two firms would separately",
    ],
    "differing-objectives-of-firms": [
        "Kinked demand curve | A demand curve that is more elastic above the current price than below it, so revenue may fall whichever way price moves",
    ],
    "regulation-provision-privatisation": [
        "*Administrative cost | The cost of running, monitoring and enforcing a policy",
    ],
    "redistribution-policies-benefits": [
        "Negative income tax | People earning below a set level receive payments through the tax system, which fall as income rises",
        "Universal basic income | A regular payment to everyone, whatever their income or work",
        "*Horizontal equity | People in similar circumstances are treated in the same way",
        "*Vertical equity | People in different circumstances are treated differently, for example higher earners paying more",
        "*Unemployment trap | Taking a job leaves someone little or no better off because benefits are lost and tax is paid",
    ],
    "monopsony-and-trade-unions": [
        "*Closed shop | A workplace where all workers must belong to a particular trade union",
    ],
    "sustainable-economic-growth": [
        "Mitigation | Action to reduce the damage growth does to the environment, including climate change",
    ],
    "commercial-banks-credit-creation": [
        "Demand deposit account | A bank account from which money can be withdrawn at any time without notice",
    ],
    "effectiveness-of-macro-policies": [
        "*Tinbergen's rule | A government generally needs at least as many independent policy instruments as it has targets",
    ],
    "population-growth-structure": [
        "*Population pyramid | A chart of a population by age group and sex",
        "*Fertility rate | The average number of children born to each woman",
        "*Malthusian theory | The idea that population could grow faster than the food supply",
    ],
    "economic-structure-pattern-of-trade": [
        "*Deindustrialisation | A long-term fall in the share of manufacturing in output or employment",
    ],
    "international-aid": [
        "*Microfinance | Small loans and other financial services for people who cannot use ordinary banks",
    ],
}

START, END = "<!-- key words -->", "<!-- /key words -->"


def _table(rows):
    return ('<div class="tw" style="overflow-x:auto"><table class="t" style="min-width:0;width:100%"><tr><th>Key word</th><th>Meaning</th></tr>'
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
        block += ('<h3>Wider words</h3><p>These go beyond the main syllabus wording. They help you understand the topic and read around it.</p>' + _table(wider))
    return page[:end] + block + "</div>\n" + END + "\n" + page[end:]
