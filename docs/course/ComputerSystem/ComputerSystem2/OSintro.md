# OS introduction

### Why Study Operating Systems
OS is highly complicated software running on most machines.

It contains many important system concepts.
> complexity hiding, performance tuning(run many tasks in the meantime), resource allocation...

Studying OS internals makes you a more capable programmer.(know how it works and how it works better)
> user（用户态）& kernel（内核态）
> In formal OS, the CPU only have a core. So the OS only support a core is running. When the CPU progress and have more cores, the OS must grow to support several cores run more tasks. Otherwise, the progress of CPU can't be embodied.

OS concepts benefit whole life.

For hacking, the more you know OS, the better hacker you are. Because the thing you are trying to hack into, probably is running an OS.

> If you can hack into the virtual machine core from your virtual machine user. Then you can hack into the VMM(virtual machine manager, link the physical computer and several virtual machines). You can hack into other's virtual machines.

For profit, Interview = coding + system design

Build your own company, ( Great system -> great product -> great company ).

### Learning Objectives
Understand operating system concepts.
> process（进程） management, CPU scheduling（进程调度，CPU调度）, synchronization（同步）, file system...

Comprehend OS concepts through programming.
> multi-threading and synchronization（多线程调度和同步）, system call（系统调用）, kernel modules（内核态）...

Get a deep understanding of how the real-world operating systems work
> You can never truly understand a concept unless you implemented (CODE) it.

### Prerequisites

+ Data Structures
+ Programming Skills
    + C
    + ASM a little 

### Course Material

+ Lecture notes
+ textbook
    + Operating System Concepts - 10th
    + Operating Systems: Three Easy Pieces (better)

## 2
### Four Compontents of a Computer System
Computer system  has four compontents:
+ **hardware** provides basic computing resources.
    + e.g. CPU, memory, I/O devices
+ **operating system** controls and coordinates use of hardware among users.
+ **application** programs use system resources to solve computing problems
    + e.g. word processors, compilers, web broswers...
+ **users** 
    + e.g., machines, other computers

### What Operating Systems Do

OS is a **resource allocator**

> it manages all resources, and it decides between conflicting requests for efficient and fair resource sharing.
>
> efficient: let the process which cost less time run first, and others follows.
> fair: let the two processes run one by one. Each of them run in a short time such as one second, and the two take turns to run. 
> 
> But if do fair, the time that waste in saving the data when the processes interrupt is so huge. Efficient can't meet.

OS is a **control program**

> it controls program execution to prevent **errors** and **improper use** of system.

### Interrupts(Hardware Interrupts) and Traps(Software Interrupts)
Interrupt transfers control to the interrupt service routine.

+ **interrupt vecter**: a table containing addresses of all the service routines.
+ incoming 

A trap is a software-generated interrupt, caused either by an error or a user request
+ an interrupt is asynchronous(异步的); a trap is synchronous(同步的).
+ e.g. system call

#### Interrupt Handling
+ Operating system preserves the execution state of the CPU
    + save registers and the program counter(PC)
+ OS determines which device caused the interrupt
    + polling
    + vectored interrupt system
+ OS handles the interrupt by calling the device's driver
+ OS restores the CPU execution to the saved state

### I/O: from System Call to Devices and Back

+ A program uses a system call to access system resources, e.g., files, network.
+ OS converts it to device access and issues I/O requests
    + I/O requests are sent to the device driver, then to the controller
    + e.g., read disk blocks, send/recieve packets
+ OS puts the program to wait (synchronous I/O) or returns to it without waiting(asynchronous I/O)
    + OS may switches to another program when the requester is waiting
+ I/O completes and the controller interrupts the OS
+ OS processes the I/O, and then wakes up the program (synchronous I/O) or send its a signal (asynchronous I/O)

### Direct Memory Access

### Storage Structure
#### Main Memory
the only large storage that CPU can directly access

+ random access
+ volatile
+ smaller space and more expensive
+ memory will lose when powered off
#### Second Storage

Magnetic disks are most common second-storage devices(HHD)

### Storage Hierarchy
Storage systems can be organized in hierarchy.

+ speed
+ cost
+ volatility

### Cache

Caching: copying information into faster storage system

data in use copied from slower to faster storage temporarily

### Computer System Arch