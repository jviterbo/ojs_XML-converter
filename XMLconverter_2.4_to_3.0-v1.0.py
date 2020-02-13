import xml.etree.ElementTree as ET
import base64 as b64


""" 
Input data
"""

#input file
infile = input("Type input file name: ")

#output file
outfile = 'output.xml'
outfile = input("Type output file name (or enter for \'output.xml\': ")

uploader = 'ojs2'
uploader = input("Uploader login: ")

title_en = ""
title_pt = ""
description_en = ""
description_pt = ""
sectitle_en = ""
sectitle_pt = ""
abbrev_en = ""
abbrev_pt = ""
arttitle_en = ""
arttitle_pt = ""
abstract_en = ""
abstract_pt = ""
content = ""
pdflocale = ""
pdffile = ""
pdffilename = ""
pdflabel = ""
volume = ""
number = ""

ksec = 0
sec = []
authors = []

#load tree
if infile!="":
    tree = ET.parse(infile)  
    print("Loaded file "+ infile)  
else:
    print("\nInput file not found\n\n")
    exit()


#issues
root = tree.getroot()

print("XML tree size: "+ str(len(root[0])))  
print("XML tree root: "+ root.tag)  

#issue
issue_node = root
for elem in root:
    if elem.tag == "volume":
        volume = elem.text
    if elem.tag == "number":
        number = elem.text
    if elem.tag == "year":
        year = elem.text
    if elem.tag == "date_published":
        date = elem.text
    if elem.tag == "title":
        if elem.attrib['locale']=="en_US":
            title_en = elem.text
        elif elem.attrib['locale']=="pt_BR":
            title_pt = elem.text
    if elem.tag == "description":
        if elem.attrib['locale']=="en_US":
            description_en = elem.text
        elif elem.attrib['locale']=="pt_BR":
            description_pt = elem.text
    if elem.tag == "section":
        sec.append(elem)
        ksec = ksec + 1
                            
f = open(outfile, "w", encoding = "utf-8")
f.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
f.write("\t<issue xmlns=\"http://pkp.sfu.ca\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" published=\"1\" current=\"1\" access_status=\"1\" xsi:schemaLocation=\"http://pkp.sfu.ca native.xsd\">\n")

if description_pt != "":
    f.write("\t\t<description locale=\"pt_BR\"><![CDATA["+description_pt+"]]></description>\n")

if description_en != "":
    f.write("\t\t<description locale=\"en_US\"><![CDATA["+description_en+"]]></description>\n")
else:
    f.write("\t\t<description locale=\"en_US\">No description was provided</description>\n")

f.write("\t\t<issue_identification>\n")

if volume != "":
    print("Volume: "+ volume + "\n")  
    f.write("\t\t\t<volume>"+volume+"</volume>\n")
    
else:
    print("Volume not found and set to 0\n")
    volume = "0"
    f.write("\t\t\t<volume>"+volume+"</volume>\n")

f.write("\t\t\t<number>"+number+"</number>\n")

f.write("\t\t\t<year>"+year+"</year>\n")

if title_pt != "":
    f.write("\t\t\t<title locale=\"pt_BR\">"+title_pt+"</title>\n")

if title_en != "":
    f.write("\t\t\t<title locale=\"en_US\">"+title_en+"</title>\n")

f.write("\t\t</issue_identification>\n")

f.write("\t\t<date_published>"+date+"</date_published>\n")

f.write("\t\t<last_modified>"+date+"</last_modified>\n")

f.write("\t\t<sections>\n")

seq = 0
for section in sec:
    print ("\nNew section found...")
    for elem in section:
        if elem.tag == "title":
            if elem.attrib['locale']=="en_US":
                sectitle_en = elem.text
                print ("...Title (en):"+ sectitle_en)
                newtitle_en = input("Type new section title in English (or type \'Enter\' for keeping \'"+sectitle_en+"\'): ")
                if newtitle_en!="":
                    sectitle_en = newtitle_en;
            if elem.attrib['locale']=="pt_BR":
                sectitle_pt = elem.text
                print ("...Title (pt):"+ sectitle_pt)
                newtitle_pt = input("Type new section title in Portuguese (or type \'Enter\' for keeping \'"+sectitle_pt+"\)': ")
                if newtitle_pt!="":
                    sectitle_pt = newtitle_pt;
        if elem.tag == "abbrev":
            if elem.attrib['locale']=="en_US":
                abbrev_en = elem.text
                print ("...Abbreviation (en):"+ abbrev_en)
                newabbrev_en = input("Type new section abbreviation in English (or type \'Enter\' for keeping \'"+abbrev_en+"\'): ")
                if newabbrev_en!="":
                    abbrev_en = newabbrev_en;
            if elem.attrib['locale']=="pt_BR":
                abbrev_pt = elem.text
                print ("...Abbreviation (pt):"+ abbrev_pt)
                newabbrev_pt = input("Type new section abbreviation in Portuguese (or type \'Enter\' for keeping \'"+abbrev_pt+"\'): ")
                if newabbrev_pt!="":
                    abbrev_pt = newabbrev_pt;
    
    if abbrev_pt == "":
        if abbrev_en != "":
            abbrev_pt = abbrev_en
        else:
            abbrev_pt = "NUL"
            abbrev_en = "NUL"
    else:
        if abbrev_en == "":
            abbrev_en = abbrev_pt
    
    if sectitle_pt == "":
        if sectitle_en != "":
            sectitle_pt = sectitle_en
        else:
            sectitle_pt = "Desconhecido"
            sectitle_en = "Unknown"
    else:
        if sectitle_en == "":
            sectitle_en = sectitle_pt
    
    f.write("\t\t\t<section ref=\""+abbrev_pt+"\" seq=\""+str(seq)+"\" editor_restricted=\"0\" meta_indexed=\"1\" meta_reviewed=\"1\" abstracts_not_required=\"0\" hide_title=\"0\" hide_author=\"0\" abstract_word_count=\"0\">\n")

    if abbrev_pt != "":
        f.write("\t\t\t\t<abbrev locale=\"pt_BR\">"+abbrev_pt+"</abbrev>\n")
        
    if abbrev_en != "":
        f.write("\t\t\t\t<abbrev locale=\"en_US\">"+abbrev_en+"</abbrev>\n")
        
    f.write("\t\t\t\t<policy locale=\"pt_BR\">Política padrão de seção</policy>\n")

    if sectitle_pt != "":
        f.write("\t\t\t\t<title locale=\"pt_BR\">"+sectitle_pt+"</title>\n")
        
    if sectitle_en != "":
        f.write("\t\t\t\t<title locale=\"en_US\">"+sectitle_en+"</title>\n")
        
    f.write("\t\t\t</section>\n")
    sectitle_en = ""
    sectitle_pt = ""
    abbrev_en = ""
    abbrev_pt = ""
    seq = seq + 1
f.write("\t\t</sections>\n")

f.write("\t\t<articles xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://pkp.sfu.ca native.xsd\">\n")

seq = 0
for section in sec:
    for elem in section:
        if elem.tag == "abbrev":
            abbrev_pt = elem.text
        if elem.tag == "article":
            for subelem in elem:
                if subelem.tag == "title":
                    if subelem.attrib['locale']=="en_US":
                        arttitle_en = subelem.text
                    if subelem.attrib['locale']=="pt_BR":
                        arttitle_pt = subelem.text
                if subelem.tag == "abstract":
                    if subelem.attrib['locale']=="en_US":
                        abstract_en = subelem.text
                    if subelem.attrib['locale']=="pt_BR":
                        abstract_pt = subelem.text
                if subelem.tag == "author":
                    authors.append(subelem)
                if subelem.tag == "galley":
                    if "locale" in subelem.attrib:
                        pdflocale = subelem.attrib['locale']
                    for galelem in subelem:
                        if galelem.tag == "label":
                            pdflabel = galelem.text
                        if galelem.tag == "file":
                            for filelem in galelem:
                                if filelem.tag == "embed":
                                    pdffile = filelem.text
                                    pdfdecode = b64.b64decode(pdffile, None, False)
                                    outpdfname = "Artigo_"+str(seq)+".pdf"
#                                    outpdf = open(outpdfname, 'wb')
#                                    print("Escrevendo arquivo ", outpdfname)
#                                    outpdf.write(pdfdecode)
#                                    outpdf.close
#                                    pdffile = b64.b64encode(pdfdecode, None)
                                    if "filename" in filelem.attrib:
                                        pdffilename = filelem.attrib['filename']
            f.write("\t\t\t<article xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" locale=\"pt_BR\" date_submitted=\""+date+"\" stage=\"production\" date_published=\""+date+"\" section_ref=\""+abbrev_pt+"\" seq=\""+str(seq)+"\" access_status=\"0\">\n")
    
            f.write("\t\t\t\t<id type=\"internal\" advice=\"ignore\">"+str(seq+5000)+"</id>\n")

            if arttitle_en != "":
                f.write("\t\t\t\t<title locale=\"en_US\">"+arttitle_en+"</title>\n")

            if arttitle_pt != "":
                f.write("\t\t\t\t<title locale=\"pt_BR\">"+arttitle_pt+"</title>\n")

            if abstract_en != "":
                f.write("\t\t\t\t<abstract locale=\"en_US\">"+abstract_en+"</abstract>\n")

            else:
                f.write("\t\t\t\t<abstract locale=\"en_US\">No abstract available</abstract>\n")

            if abstract_pt != "":
                f.write("\t\t\t\t<abstract locale=\"pt_BR\">"+abstract_pt+"</abstract>\n")

            else:
                f.write("\t\t\t\t<abstract locale=\"pt_BR\">Nenhum resumo disponível</abstract>\n")

            f.write("\t\t\t\t<authors xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://pkp.sfu.ca native.xsd\">\n")

            for author in authors:
                if "primary_contact" in author.attrib:
                    if author.attrib['primary_contact']=="true":
                        f.write("\t\t\t\t\t<author primary_contact=\"true\" include_in_browse=\"true\" user_group_ref=\"Author\">\n")
                    else:
                        f.write("\t\t\t\t\t<author primary_contact=\"false\" include_in_browse=\"true\" user_group_ref=\"Author\">\n")
                else:
                    f.write("\t\t\t\t\t<author primary_contact=\"false\" include_in_browse=\"true\" user_group_ref=\"Author\">\n")
                
                for autelem in author:
                    if autelem.tag == "firstname":
                        f.write("\t\t\t\t\t\t<firstname>"+autelem.text+"</firstname>\n")
                        
                    if autelem.tag == "lastname":
                        f.write("\t\t\t\t\t\t<lastname>"+autelem.text+"</lastname>\n")
                        
                    if autelem.tag == "middlename":
                        f.write("\t\t\t\t\t\t<middlename>"+autelem.text+"</middlename>\n")
                        
                    if autelem.tag == "affiliation":
                        f.write("\t\t\t\t\t\t<affiliation locale=\"pt_BR\">"+autelem.text+"</affiliation>\n")
                        
                    if autelem.tag == "country":
                        f.write("\t\t\t\t\t\t<country>"+autelem.text+"</country>\n")
                        
                    if autelem.tag == "email":
                        f.write("\t\t\t\t\t\t<email>"+autelem.text+"</email>\n")
                        
                f.write("\t\t\t\t\t</author>\n")
            f.write("\t\t\t\t</authors>\n")
            
            f.write("\t\t\t\t<submission_file xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" stage=\"submission\" id=\""+str(seq+5000)+"\" xsi:schemaLocation=\"http://pkp.sfu.ca native.xsd\">\n")

            f.write("\t\t\t\t\t<revision number=\""+str(seq+5000)+"\" genre=\"Article Text\" filename=\"artigo"+str(seq+1)+".pdf\" viewable=\"true\" date_uploaded=\""+date+"\" date_modified=\""+date+"\" filesize=\""+str(len(pdffile))+"\" filetype=\"application/pdf\" user_group_ref=\"Author\" uploader=\""+uploader+"\">\n")

            f.write("\t\t\t\t\t\t<name locale=\""+pdflocale+"\">"+outpdfname+"</name>\n")

            f.write("\t\t\t\t\t\t<embed encoding=\"base64\">"+pdffile+"</embed>\n")

            f.write("\t\t\t\t\t</revision>\n")
            f.write("\t\t\t\t</submission_file>\n")

            f.write("\t\t\t\t<article_galley xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" approved=\"false\" xsi:schemaLocation=\"http://pkp.sfu.ca native.xsd\">\n")

            f.write("\t\t\t\t\t<id type=\"internal\" advice=\"ignore\">"+str(seq+5000)+"</id>\n")

            f.write("\t\t\t\t\t<name locale=\""+pdflocale+"\">"+pdflabel+"</name>\n")

            f.write("\t\t\t\t\t<seq>0</seq>\n")

            f.write("\t\t\t\t\t<submission_file_ref id=\""+str(seq+5000)+"\" revision=\""+str(seq+5000)+"\"/>\n")

#            f.write("\t\t\t\t\t<remote src=\"https://webmedia.org.br/anais/WCT-Video/p187Roesler.pdf\"/>\n")
            f.write("\t\t\t\t</article_galley>\n")
            f.write("\t\t\t</article>\n")
            arttitle_en = ""
            arttitle_pt = ""
            abstract_en = ""
            abstract_pt = ""
            content = ""
            pdflocale = ""
            pdffile = ""
            pdffilename = ""
            pdflabel = ""
            authors = []
            seq = seq + 1
    abbrev_pt = ""
f.write("\t\t</articles>\n")
f.write("\t</issue>\n")
f.close
print("Output written to "+outfile)
