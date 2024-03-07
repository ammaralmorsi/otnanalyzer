# OTN Frame Analyzer

## System Design
The OTN analyzer reads its input from a file. This file contains multiple lines, each representing a single frame. Each frame is a sequence of space-separated decimal values, 
where each value represents a byte between 0 and 255. In simpler terms, the file is a collection of lines, 
where each line is a series of numbers between 0 and 255, separated by spaces, that define a unit of data for the analyzer.
Our first task is to process the input file. We can achieve this by reading it and storing the data in a Python object. We'll use a list of lists, where each inner list represents a single frame,
and each element within that inner list represents a byte value.
Once we have the data stored as a list of lists, we will need to convert the decimal byte values within each frame to their corresponding hexadecimal representation.
All frames within the list of lists share a consistent type, which can be either **Client Signal,** **OPU,** **ODU,** or **OTU.** This ensures that each frame adheres to a specific structure and interpretation within the OTN protocol.
To improve the OTN analyzer's structure and readability, it is recommend to use a class-based approach. This class would accept the list of lists containing the frame data as input and be responsible for constructing individual frame objects.
Instead of a list of lists representing the raw hexadecimal bytes, the output would be a list containing objects of specific types like **ClientSignal**, **OPU**, **ODU**, or **OTU**, each encapsulating the parsed frame data.

![image](https://github.com/ammaralmorsi/otnanalyzer/assets/88221190/867aeb93-eefd-4d6a-8763-7df6deafa746)

## Supported Fields
OTN frames are composed of various fields, each with a designated location within the frame structure. These fields can range in size, encompassing multiple bytes for larger data, or just a single bit, or potentially a few bits. 
Fortunately, the OTN analyzer doesn't need to process all the frame fields, but only those relevant to "VirtualOTN." Here's a breakdown of the fields of interest for each frame type:

**OPU Frames:**

-   **JC{i}**: Where i ranges from 1 to 6 (identified as individual fields).
-   **NJO/OMFI**: Treated as a single field.
-   **PJO**: Single field.
-   **PSI**: Single field.

**ODU Frames:**

-   **TCM{i}**: Where i ranges from 1 to 6 (identified as individual fields).
-   **PM/TCM**: Treated as a single field.
-   **PM**: Single field.
-   **EXP**: Single field.
-   **APS/PCC**: Treated as a single field.
-   **GCC{i}**: Where i ranges from 1 to 2 (identified as individual fields).

**OTU Frames:**

-   **SM**: Single field.
-   **GCC0**: Single field.
-   **OSMC**: Single field.

**Frame Alignment:**

-   **FAS**: Single field.
-   **MFAS**: Single field.

## OTN Frame Structure
![image](https://github.com/ammaralmorsi/otnanalyzer/assets/88221190/27c802e7-1535-4285-9a03-dada2da90fe0)

### OPU Frame
![image](https://github.com/ammaralmorsi/otnanalyzer/assets/88221190/5dd9016b-041f-4c41-81f0-026c3c9ef49c)
![image](https://github.com/ammaralmorsi/otnanalyzer/assets/88221190/6f697970-fdb4-4dee-9eb5-43224dcc5567)

### ODU Frame
![image](https://github.com/ammaralmorsi/otnanalyzer/assets/88221190/d9c5b906-3760-4d49-9cdd-72e00237398b)
![image](https://github.com/ammaralmorsi/otnanalyzer/assets/88221190/1fe198e1-1155-4dcd-b379-5f80eb62e858)
![image](https://github.com/ammaralmorsi/otnanalyzer/assets/88221190/333881a6-bd19-4342-908c-bf2883669bf9)
![image](https://github.com/ammaralmorsi/otnanalyzer/assets/88221190/7d166225-21b1-4dca-8a4c-047164be6ae4)
![image](https://github.com/ammaralmorsi/otnanalyzer/assets/88221190/6bec511f-d4f8-4259-92b0-e162703eec7e)

### OTU Frame
![image](https://github.com/ammaralmorsi/otnanalyzer/assets/88221190/631931ee-0b24-428c-a6ef-0a37ae3e4126)
![image](https://github.com/ammaralmorsi/otnanalyzer/assets/88221190/8c08fd68-1fbe-471d-8fcd-0bfef201cb3c)

### Frame Alignment
![image](https://github.com/ammaralmorsi/otnanalyzer/assets/88221190/c9dc84f6-d46b-4bd2-b269-3c6d4d63741b)

## References
[OTN Standard](https://www.itu.int/rec/T-REC-G.709-202006-I/en)





