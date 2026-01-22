CHALK UNIVERSAL | 4.1 - SYSTEM MANUAL

OVERVIEW CHALK Universal is a high-performance terminal environment and scripting kernel. It allows for advanced file management, system telemetry, and hardware interaction through a standardized command set.





SYSTEM GRAMMAR AND SYNTAX To ensure the kernel processes commands correctly, follow these rules:

CASE SENSITIVITY: Commands must be entered in UPPERCASE (e.g., ECHO, SET).

VARIABLE CALLING: Use a "$" prefix to recall stored data (e.g., $USER).





LOGICAL BLOCKS: Commands within IF or ALWAYS statements must be wrapped in curly braces: { command }.
example: if var == var1 {[run code hear]}

SPACING: Use exactly one space between a command and its argument.

HARDWARE SPACING: Use two spaces for hardware-level pin commands: PIN 2 HIGH.

COMMAND REFERENCE:

FILE SYSTEM,

DIR: Lists all files on the current drive.


TYPE [file]: Displays the contents of a file.



NANO [file]: Opens the multi-line file editor; type SAVE on a new line to finish.




RUN [file]: Executes a .chk or .bat script. if you are not on windows DO NOT RUN A .BAT FILE


DEL [file]: Permanently deletes the specified file.

MKDIR [name]: Creates a new directory.


WIPE: Formats the drive (requires 'Y' confirmation). WARNING THIS WILL WIPE YOUR DRIVE. YES DEPENDING ON WHERE YOU ARE IT  W I L L DELEAT IT ALL!!!  

LOGIC AND VARIABLES

SET [var]=[val]: Stores a value into a system variable.



INPUT "[msg]" [var]: Prompts the user and saves the response to a variable.

IF [v1] == [v2] {cmd}: Executes command only if the condition is met.


SLEEP [n]: Pauses execution for [n] seconds.


ALWAYS {cmd}: Starts an infinite loop.

STOP: Immediately breaks out of an active loop.

TELEMETRY AND SYSTEM

TEMP: Displays internal CPU temperature.


STAT: Shows drive capacity and RAM health.


UPTIME: Displays seconds elapsed since boot.

SYSINFO: Shows CPU model and clock speed.

DATE: Displays current system date.


UTILITIES

ECHO [text]: Prints text to the display.


CLS: Clears the screen and resets the header.



SHELL [cmd]: Directly executes a native Windows command.

EXIT: Performs a safe shutdown of the kernel.


GETTING STARTED

Run the master kernel file using a Python interpreter.

Type HELP to view the command registry.

Use NANO to create your first .chk script.

Use RUN to execute your saved automation.

SHIELD NOTICE The System32 Safety Shield is active. Access to DEL, WIPE, and NANO is restricted in protected Windows system directories to prevent accidental data loss.





during the prosses of creating chalk, there were some ideas that were left out, but the "idea of the idea" still remains.
example: chalk used to need a stk (stack, a programing language that used to accompany chalk, stack would tell chalk what "virtual machine" it is running on, like the clock speed, max cpu temp, ram ect) to even boot, but now chalk no longer needs a stk file to boot, because the "virtual hardwear" is pre-programmed into chalk, but just in case you are provided with a bios.stk file. 


there is also another version of chalk (chalk v4.1) that only runs on a specific computer, file system ect but that will not be released to the public because it only run on a very specific computer. have fun!
