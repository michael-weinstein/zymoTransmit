# Zymo Research Transmit: Simple Public Health Data Transmission
##### A collaboration between UCLA and Zymo Research

---

We are honored to be playing an important role in the response to COVID-19.  To assist with that, we have chosen to make this program available as free, open-source academic/industry collaborative software for all to use with our support.  The release of this software has been supported by the UCLA Molecular, Cell, and Developmental Biology Department as well as the Quantitative and Computational Biosciences Institute (the Collaboratory in particular) in collaboration with Zymo Research.

     Be quick, but don't hurry.
                                 – John Wooden
                                 
At UCLA, our core mission can be summarized into **Education, Research, and Service**. 

At Zymo Research, our vision is, "*To have a positive impact in the biomedical field and to contribute to the greater good of humanity*". 

It is with these principles guiding our efforts that we offer this software package free to use to facilitate California's epidemiology efforts during this challenging time.


#### Publication
At present, there is not publication planned for this software.  If anybody in the public health/epidemiology field wishes to collaborate on one (especially the Fielding School of Public Health), please contact us.

## Quick Start Guide
This Program was written in Python 3.6.4.  It should work with other version of 3.6 and most likely later versions as well.
Earlier versions may have some difficulties. Please report any compatibility problems you may have and I will see about addressing them if you really must run on a different version of Python.

If you do not already have the Python language installed on your computer, you can download the web-based installer from this page on [python.org](https://www.python.org/downloads/release/python-364/) or directly from [here](https://www.python.org/ftp/python/3.6.4/python-3.6.4-amd64-webinstall.exe) on a Windows computer.  **During Python installation, be sure to enable Python in your PATH variables, as that will make this program much easier to run in the future.  Also be sure to approve installation of Tcl/Tk and PIP, as those will also contribute to making this easier to run in the future.**

If your operating system is Windows, your commands will start with "python" as seen below.
If your OS is Mac or Linux, you will need to start with "python3" instead of "python"


#### Running and setting up without terminal commands

This program can run on a Windows computer with Python installed with little to no use of terminal commands (although terminal will still be used to give you information).  **This is facilitated by having Python available on your *PATH* variable along with PyTk and PIP.** Forgot to enable those? Rerun the installer from above and it will give you the option to modify your installation and fix that.
* Download this program as a zipped archive from GitHub
* Extract all of the files to a convenient location.
* Go to the main folder of this program where you extracted it.  You should see several files including:
  * **zymoResearch.py** (The main executable source code for this system)
  * **SETUP.bat** (Batch script to install required Python packages)
  * **RUN.bat** (Batch script to run the main program)
* Double-click *SETUP.bat*. You should see a terminal window open with some text crossing it and then it will quickly close. This should complete the installation of required Python packages. You should only have to do this before running the program the first time.
* Gather all of your lab information as well as your enrollment letter for CalREDIE, you will need this in the next step.
* Double-click  *RUN.bat*. This will be how you launch the program from here on out.
  * The first time you run, you will get a text editing window for your *config.txt* file.  Fill in as many fields as possible using your lab information or the enrollment letter's credentials.
    * This *config.txt* file will be in the same folder as your executable files, should you need to edit it again.  
    * Please avoid editing this file in Microsoft Word or other word processor programs, as they can introduce strange characters that will corrupt this file. 
    * A simple text editor will avoid this problem and can be launched by starting the program and selecting the *config.txt* file from the main directory.
  * The next time you run this program, you will need to install your certificate.  It should have arrived from CDPH as a file ending with *.pfx* and it should have a password in the enrollment document (please be sure not to confuse this with your SOAP gateway password)
    * Run the program and select the certificate file ending in *.pfx* in the file browser that pops up.
    * A window will pop up asking for the certificate password. Enter the password and either click *ok* or press *Return* to proceed.
      * You can paste the password into the prompt using *ctrl + v* after copying it from the document (recommended)
    * The terminal window should say that the certificate was converted
    * Press enter to end the program
* At this point, setup should be complete. Run the program for submission now and in the future by double-clicking *RUN.bat* as before and selecting a tab-delimited text file (ending in *.txt*) or a comma-separated values (CSV) file ending in *.csv*.  
  * You can also edit your config at any time by selecting your *config.txt* file
    * **Once CalREDIE has approved you for submitting to the production environment**, you will need to edit this file to reflect that. Simply change the *In Testing* value to *FALSE* from its default value of *TRUE* 
  * If your lab is generating raw HL7 data for submission, make sure your HL7 file ends with *.hl7* and select the file containing the HL7 data for upload.  
    * This program will not edit or inspect your HL7 data in any way, other than the very beginning and very end of the block to clean up any potentially unwanted non-printing characters.
* Be sure to check the terminal window after job completion to see any error messages that were generated.  Copies of all data submitted and receipts for data transmission can be found in the *transmissionLogs* folder.

#### Downloading and setting up the program

* You will need to download this program from Github.  If you know how to do this via command line git commands, please use those.
* Otherwise, you will need to click the download link above and download as a zip file.
* Once that is complete, you will want to extract the files to the desired folder.
* With the files extracted, open a command prompt go into the directory containing the zymoTransmit program, you should see a file called "zymoTransmit.py"
* Copy your health department-supplied certificate file (ending in .pfx) to this directory

Install required python packages on Windows:
```
pip install -r requirements.txt
```
Install the required python packages on MacOS or Linux:
```
pip3 install -r requirements.txt
```
Set up your config file and required folders (don't forget to put in userID and password from the document sent by the health department). A file editor window will appear to help with this if GUI functionality is available.

***Remember to save before exiting***

If you need to edit this file in the future, it can be found at ```zymoTransmit/zymoTransmitSupport/config.py``` 
```
python zymoTransmit.py
```
Convert your certificate for use (if you do not supply a file name, a file browser window will appear if GUI functionality is available)
```
python zymoTransmit.py -c [fileName.pfx]
```
Test your connection
```
python zymoTransmit.py -t
```
If the connection worked, you should see something similar to:
```
Server returned:

Prefixes:
     xsd: http://www.w3.org/2001/XMLSchema
     ns0: urn:cdc:iisb:2011

Global elements:

     ns0:MessageTooLargeFault(ns0:MessageTooLargeFaultType)
     ns0:SecurityFault(ns0:SecurityFaultType)
     ns0:UnsupportedOperationFault(ns0:UnsupportedOperationFaultType)
     ns0:connectivityTest(ns0:connectivityTestRequestType)
     ns0:connectivityTestResponse(ns0:connectivityTestResponseType)
     ns0:fault(ns0:soapFaultType)
     ns0:submitMessage(ns0:submitMessageRequestType)
     ns0:submitMessageResponse(ns0:submitMessageResponseType)
...
```
If you see an exception, please check your Internet connection and try again or reach out for support.  

If this works, you are ready to transmit!


#### Preparing a report
The program should have come packaged with a file called ```templateSubmission.txt``` this tab-delimited text file will open in Microsoft Excel and can help you start putting together reports for submission.  Please try to fill in all fields if possible to avoid having submissions rejected for missing data.  Fields that can accept telephone numbers can also accept emails if that is the preferred method of contact for the patient or provider.  

To find out an appropriate LOINC code to describe your test:
```
python zymoTransmit.py -l
```
To find out an appropriate SNOMED code to describe your specimen:
```
python zymoTransmit.py -s
```
There are several codes related to SARS-CoV-2 testing available, so please look carefully for the one that most closely describes your test method and sample.

When preparing this report, please avoid the use of placeholders for missing or non-applicable data; **if something has no value, either due to being non-applicable or missing, leave it blank**!  This will avoid any confusion or potential to treat a value such as "N/A" as real data.  Several potential result terms have already been programmed in to be interpreted by the program as positive, negative, or other results.  These terms can be seen in the config.py file in zymoTransmitSupport and terms can be added or removed if needed.


#### Transmitting results
Once a report has been filled out correctly, submitting reports requires a simple command:
```
python zymoTransmit.py [reportName.txt]
```
Use the file name for your report in place of the bracketed text above. 

If you are unsure how to find the file, leave it blank and a file browser window will open on your screen to help you find it if GUI functionality is available.

#### Command line arguments
Commands are formulated as follows:
```
python zymoTransmit.py [argument] [filename if needed]
```

| Long Name        | Short Name           | Notes  
| --------------- |:--------------:|:--------|
--help	|	-h	|	Displays a list of arguments 
--convertCertificate	|	-c	|	Loads and converts a certificate. Requires a file and will prompt for one if missing. May ask for certificate password.
--editConfig	|	-e	|	Edit the configuration file.  ***Remember to save and exit with done***
--testConnection	|	-t	|	Tests the connection to the health department, run as a final step of setup
--snomed	|	-s	|	Display relevant SNOMED codes for specimen types
--loinc	|	-l	|	Display relevant LOINC codes for testing types
--cdph  | | Accept a CDPH-formatted CSV file (run using **CDPH.bat**)


## OUTPUT
The key output is sent over the Internet to the agency receiving the test reports.  Local outputs will be as follows:

The transmission logs folder will get two files per session.  Both will contain timestamps in the name and one will be called resultText[*timestamp*].hl7, which will contain the raw HL7 data transmitted during the session.  The other will be called submissionLog[*timestamp*].txt and will contain receipts for each patientID:specimenID combination sent.  **If a submission was rejected by the gateway, the reason(s) will be found in this file.**

An additional file called rejects.csv will be created at the start of each run in the program root folder if it does not already exist.  This file will contain lines for any results that were either unable to be converted to HL7 (often due to uninterpretable results) or any lines that were not successfully transmitted through the gateway (this could be due to a failure in the gateway itself or something invalid in the data).  Check the submissionLog file mentioned in the previous paragraph to determine if corrections are needed before retransmission.  This CSV file can be opened in a spreadsheet application (such as Microsoft Excel) to fix any incorrect information.  The file can then be renamed, keeping the CSV extension and run through the program as new data of the original format and a new rejects file will be started automatically.  This practice should make retransmission of failed attempts easier for the user while minimizing duplicate transmissions seen by the gateway.

## Contributing

We welcome and encourage contributions to this project from the microbiomics community and will happily accept and acknowledge input (and possibly provide some free kits as a thank you).  We aim to provide a safe, positive, and inclusive environment for contributors that is free of any harassment or excessively harsh criticism. Our Golden Rule: *Treat others as you would like to be treated*.

## Versioning

We use a modification of [Semantic Versioning](https://semvar.org) to identify our releases.

Release identifiers will be *major.minor.patch*

Major release: Newly required parameter or other change that is not entirely backwards compatible with report formats
Minor release: New optional parameter
Patch release: No changes to parameters

## Current Version

The current major release contains all initial functionality plus some additional features designed to help the California Department of Public Health clear backlogged data using their existing form.  Many of these extended features will also help other users with their submissions.  Essential features covered include transmission of data from this program's preferred table format (either CSV or tab-delimited text), transmission of a large block of HL7 data, transmission of a folder with individual HL7 data blocks, transmission of a CDPH-formatted CSV file, and handling of results that fail to transmit for various reasons.

This major release has been nicknamed Imahara's Pudding Cup after [Grant Imahara](https://en.wikipedia.org/wiki/Grant_Imahara), a popular advocate of STEAM education and performing random acts of kindness for others.

## Authors

- **Michael M. Weinstein** - *Project Lead, Programming and Design* - [michael-weinstein](https://github.com/michael-weinstein)
  - Scientist at Zymo Research and Adjunct Professor of Molecular, Cell, and Developmental Biology at UCLA and Member of the QCB Collaboratory
 - For support, please contact michael.weinstein -atSymbol- ucla.edu or call us at (949) 679-1190 

See also the list of [contributors](https://github.com/Zymo-Research/zymoTransmit/contributors) who participated in this project.

## License

This project is licensed under the GNU GPLv3 License - see the [LICENSE](https://github.com/Zymo-Research/zymoTransmit/blob/master/LICENSE) file for details.
This license restricts the usage of this application for non-open sourced systems. Please contact the authors for questions related to relicensing of this software in non-open sourced systems.

## Acknowledgments

We would like to thank the following, without whom this would not have happened:
* The Python Foundation
* The staff at Zymo Research
* The UC System
* Pangea Laboratory
* The California Department of Public Health
* Our customers

---------------------------------------------------------------------------------------------------------------------

#### If you like this software, please let us know at info@zymoresearch.com.
#### Please support our continued development of free and open-source microbiomics and other applications by checking out the latest COVID-19 related offerings at [Zymo Research](https://www.zymoresearch.com/pages/covid-19-efforts) and our latest microbiomics offerings from [ZymoBIOMICS](https://www.zymoresearch.com/pages/zymobiomics-portfolio).
