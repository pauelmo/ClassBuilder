# classbuilder.py
# 🐍

from cmath import e
import io
from msilib.schema import Class
import os.path

class ClassBuilder(object):
    def __init__(
        self,
        class_contents,
        class_name,
        console_output,
        field_count,
        field_list,
        input_file,
        input_file_exists,
        output_file):
        self.class_contents = class_contents,
        self.class_name = class_name,
        self.console_output = console_output,
        self.field_count = field_count,
        self.field_list = field_list,
        self.input_file = input_file,
        self.input_file_exists = input_file_exists,        
        self.output_file = output_file
        
        
    @staticmethod
    def init(ClassBuilder):
        
        try:
            if ClassBuilder.class_contents is None:
                ClassBuilder.class_contents = ""
        except:
            ClassBuilder.class_contents = ""
        
        try:
            if ClassBuilder.class_name is None:
                ClassBuilder.class_name = "MyClass"
        except:
            ClassBuilder.class_name = "MyClass"
            
        try:
            if ClassBuilder.console_output is None:
                ClassBuilder.console_output = True
        except:
            ClassBuilder.console_output = True
        
        try:
            if ClassBuilder.field_count is None:
                ClassBuilder.field_count = 0
        except:
            ClassBuilder.field_count = 0
            
        try:
            if ClassBuilder.field_list is None:
                ClassBuilder.field_list = []
        except:
            ClassBuilder.field_list = []
            
        try:
            if ClassBuilder.input_file is None:
                ClassBuilder.input_file = "class.txt"
        except:
            ClassBuilder.input_file = "class.txt"
            
        try:
            if ClassBuilder.input_file_exists is not True:
                ClassBuilder.input_file_exists = False
        except:
            ClassBuilder.input_file_exists = False
                    
        try:
            if ClassBuilder.output_file is None:
                ClassBuilder.output_file = "_" + ClassBuilder.class_name + ".py"
        except:
            ClassBuilder.output_file = "_" + ClassBuilder.class_name + ".py"
            
        return ClassBuilder
    
    
    @staticmethod
    def create_class(ClassBuilder):
        
        ClassBuilder = ClassBuilder.init(ClassBuilder)
        
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("ClassBuilder 1.0")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Class Name: " + str(ClassBuilder.class_name))
        print("Input File: " + str(ClassBuilder.input_file))
        print("Output File: " + str(ClassBuilder.output_file))
        
        ClassBuilder = ClassBuilder.generate_class_list_from_file(ClassBuilder)
        
        # bail out entirely IF:
        # 1. no input file of any kind exists, and / or...
        # 2. no class field entries were specified in the "field_list"
        # list parameter:
        if (ClassBuilder.input_file_exists == False and
            len(ClassBuilder.field_list) == 0):
            error_message = (
                    "Neither an input field or " + "\"" + "field_list" + "\"" +
                    " exists.  Either create a list with a custom file name, " +
                    "and specify it in the " + "\"" + "input_file" + "\"" +
                    ", or create the default " + "\"" + "class.txt" + "\"" +
                    " input file and add your desired class field entries " +
                    "there, OR... create an explicit list of desired class " +
                    "field entries in the " + "\"" + "field_list" + "\"" +
                    " list, excecute again.")
            print("")
            print(error_message)
            
            return ClassBuilder # bail out
        
        else:
            ClassBuilder = ClassBuilder.create_class_def(ClassBuilder)
            ClassBuilder = ClassBuilder.create_class_init(ClassBuilder)
            
            
            print("Number of fields: " + str(ClassBuilder.field_count))
            print("")
            print("Fields:")
            print("----------")
            for each_field in ClassBuilder.field_list:
                print(str(each_field))
            
            print("----------")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            
            class_header = (
                "# " + ClassBuilder.output_file + " " + "\n" +
                "# " + "🐍" + "\n")
            
            try:            
                ClassBuilder.class_contents = (
                    class_header + "\n" + "\n" +
                    ClassBuilder.class_contents)
                            
                with open(ClassBuilder.output_file, "w+", encoding="utf-8") as f:
                    f.write(ClassBuilder.class_contents) 
                    #str(symbol.encode('utf-8')))
                                        
            except:
                error_message = (
                    "Encountered an error attempting to create class file:" + "\n" +
                    "========================" + "\n" +
                    "Details:" + "\n" +
                    "========================" + "\n" +
                    "Class Name: " + str(ClassBuilder.class_name) + "\n" +
                    "Input File: " + str(ClassBuilder.input_file) + "\n" +
                    "Output File: " + str(ClassBuilder.output_file) + "\n") 
                print(error_message)
                print("")
                
            print("Generated " + str(ClassBuilder.output_file + " class file."))
            print("")
            print("")
            print("")
            
            if ClassBuilder.console_output is True:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(str(ClassBuilder.output_file) + " (contents):")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                
                class_file_contents = ""
                new_class_file = "_" + str(ClassBuilder.output_file)
                try:
                    with open(str(ClassBuilder.output_file), "r+", encoding="utf-8") as f:
                        f.readlines()
                        
                        f.seek(0)
                        for each_line in f:
                            if "🐍" in each_line:
                                print("#")
                            else:
                                class_file_contents = class_file_contents + each_line
                                
                    print(str(class_file_contents))
                
                except:
                    print(
                        "Encountered an error attempting to read the " +
                        "new-created class file contents in " + 
                        str(ClassBuilder.output_file) + ".")
                
        return ClassBuilder


    @staticmethod
    def create_class_def(ClassBuilder):
        
        # three "spaces" (subsequently making first 
        # character then start at "4")
        indent = "    " 
        
        ClassBuilder.class_contents = (
            "class " + ClassBuilder.class_name + 
            "(object):" + "\n" +
            indent + "def __init__(" + "\n" +
            indent + indent + "self,")
        
        # if the class field is the last one in the list, then 
        # concatenate with "):", otherwise concatenate with ",".  
        field_count = 1
        for each_field in ClassBuilder.field_list:
            if field_count == ClassBuilder.field_count:
                ClassBuilder.class_contents = (
                    ClassBuilder.class_contents + "\n" +
                    indent + indent + each_field + "):")
            else:
                ClassBuilder.class_contents = (
                    ClassBuilder.class_contents + "\n" +
                    indent + indent + each_field + ",")
                
            field_count+=1
            
        # if the class field is NOT the last one in the list,
        # then concatenate with ",", otherwise add nothing:
        field_count = 1
        
        if len(ClassBuilder.field_list) == 0:
                error_message = (
                    "Neither an input field or " + "\"" + "field_list" + "\"" +
                    " exists.  Either create a list with a custom file name, " +
                    "and specify it in the " + "\"" + "input_file" + "\"" +
                    ", or create the default " + "\"" + "class.txt" + "\"" +
                    " input file and add your desired class field entries " +
                    "there, OR... create an explicit list of desired class " +
                    "field entries in the " + "\"" + "field_list" + "\"" +
                    " list, excecute again.")
                print("")
                print(error_message)
                return ClassBuilder # bail out
        else:
            for each_field in ClassBuilder.field_list:
                if field_count == ClassBuilder.field_count:
                    ClassBuilder.class_contents = (
                        ClassBuilder.class_contents + "\n" +
                        indent + indent + 
                        "self." + each_field + " = " + each_field)
                else:
                    ClassBuilder.class_contents = (
                        ClassBuilder.class_contents + "\n" +
                        indent + indent + 
                        "self." + each_field + " = " + each_field + ",")
                    
                field_count+=1
        
        return ClassBuilder
    
    
    @staticmethod
    def create_class_init(ClassBuilder):
        
        # three "spaces" (subsequently making first 
        # character then start at "4")
        indent = "    "
        indent2 = indent * 2
        indent3 = indent * 3
        indent4 = indent * 4
        
         
        init_header = (
            indent + "@staticmethod" + "\n" +
            indent + "def init(" + 
            ClassBuilder.class_name + "):" + "\n" + "\n")
        
        # add the nedaer contents to previously-generated contents:
        ClassBuilder.class_contents = (
            ClassBuilder.class_contents + "\n" + "\n" + "\n" +
            init_header)
        
        # add the field initializations and default values to the
        # "class contents":
        field_count = 1
        for each_field in ClassBuilder.field_list:
            # if field is the universal "console output" field,
            # then set it to "False" for default, while all other
            # fields will be set to an empty string value for default:            
            if each_field == "console_output":
                init_contents = (
                indent2 + "try:" + "\n" +
                indent3 + "if " + ClassBuilder.class_name + 
                "." + str(each_field) + " is None:" + "\n" +
                indent4 + ClassBuilder.class_name +
                "." + str(each_field) + " = " + "False" + "\n" +
                indent2 + "except:" + "\n" +
                indent3 + ClassBuilder.class_name +
                "." + str(each_field) + " = " + "False" + "\n" + "\n")
            else:
                init_contents = (
                indent2 + "try:" + "\n" +
                indent3 + "if " + ClassBuilder.class_name + 
                "." + str(each_field) + " is None:" + "\n" +
                indent4 + ClassBuilder.class_name +
                "." + str(each_field) + " = " + "\"" + "\"" + "\n" +
                indent2 + "except:" + "\n" +
                indent3 + ClassBuilder.class_name +
                "." + str(each_field) + " = " + "\"" + "\"" + "\n" + "\n")
                
            ClassBuilder.class_contents = (
                ClassBuilder.class_contents + init_contents)
        
            field_count+=1            
        
        return ClassBuilder

  
    @staticmethod
    def generate_class_list_from_file(ClassBuilder):
        
        ClassBuilder.field_count = 0
        
        if ClassBuilder.field_list is None:
            ClassBuilder.field_list = [] # ensure reset ONLY if empty
        
        for each_field in ClassBuilder.field_list:
            ClassBuilder.field_count+=1
               
        # check to see if the specified (or "unspecified" default of class.txt) 
        # input file exists.  If it exists, move forward and extract the contents.
        # if the input file does NOT exist, then only check for entries for
        # "field_list" list entry.  Then...
        # open the input field list file, delete any blank lines, 
        # read all the lines, then sort them alphabetically and 
        # write them back to the input file:
        ClassBuilder.input_file_exists = os.path.exists(ClassBuilder.input_file)
        
        if ClassBuilder.input_file_exists is True:
            try:
                with open(ClassBuilder.input_file, 'r+', encoding="utf-8") as f:
                    lines = f.readlines()
                    lines = sorted(lines)
                    
                    f.seek(0)
                    for line in lines:
                        if line != "\n":
                            f.write(line)
                            line = (str(line.strip('\n')))
                            ClassBuilder.field_list.append(line)
                            #ClassBuilder.field_count+=1

                    f.truncate()
                    
                    # sort the fields alphabetically so that they will be
                    # in alphabetical order when the class implementation 
                    # is built out and saved to clss file:           
                    ClassBuilder.field_list = sorted(ClassBuilder.field_list)    
                    ClassBuilder.field_count = len(ClassBuilder.field_list)
                    
            except:
                error_message = (
                    "Encountred an error attempting to generate a class list " +
                    "from " + str(ClassBuilder.input_file) + ". Please check " +
                    "this file for invalid entries or other potential issues.")
                print(error_message)
        
        return ClassBuilder