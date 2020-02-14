# ojs_XML-converter
XML converter specially created to convert files created by OJS 2.4 Native XML Plugin, allowing them to be imported by OJS 3.X. 

IMPORTANT: The import process will only be succesful if the sections described in the XML exist in the journal, and the section title and abbreviation registered in the XML file are identical to those configured in OJS.

At the beginning, the converter prompts for the following inputs:

    1) Name of the XML file to be converted, which must be a journal issue exported from an OJS 2.4 platform, 
       using Native XML Plugin.

    2) Name of the output file, i.e., the XML file converted to be imported by an OJS 3.X platform, 
       using Native XML Plugin. As default, the file is identified  with the input file name prefixed by "output-"
	
    3) Login name of the user that will import this file.

During the convertion process, for each section identified in the input file, the converter will ask for the confirmation or modification of the following pieces of information:

    1) The section title in Portuguese, if it is available.

    2) The section title in English, if it is available.

    3) The section abbreviation in Portuguese, if it is available.

    4) The section abbreviation in English, if it is available.
