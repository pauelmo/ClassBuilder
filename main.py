# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# NOTE:
#
# 1. 
# If no "class name" is specified, it will create
# a class name by the name of "MYClass" as a defaut.
# 
# 2. 
# If no "output file" is specified, it will create a
# class file using the "class name", but with a "_"
# character concatenated to the front of the putput
# class file.  This way, if the file name is not 
# specified (or user is being lazy), the class file
# will be intuitively named the same as the class name,
# but will include underscore character at the front so
# that it will not overwrite or delete any possible 
# class file that may already exist with the same name,
# blut also so that the new file will appear toward the
# top of the file list in the project explorer panel, so
# that the new file will be more likely to be spotted
# when it is generated, as well as making it easier to
# find.
#
# 3. 
# If no "input file" name is specified, it will look
# for a file named "class.txt" as a default for input.
#
# 4.
# Another option is that the "input file" can be 
# completely overridden / ignored instead by 
# explicitly specifying class field entries, by 
# adding entries to the "field_list" list field,
# (e.g. cb.field_list = ["env_id", "env_name"]).
# ALSO:...
# IF an explicit "input file" was specified (or the 
# default "class.txt" was created and populated with
# fields), AND... there are additional entries 
# explicitly added to "field_list" field in the code,
# then Class Builder will create a hybrid / combination 
# class file with ALL fields from "class.txt" (or other
# alaternate) input file with entries), AND ALL fields
# that were explicitly specified in "field_list".
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from classbuilder import ClassBuilder

cb = ClassBuilder
cb = ClassBuilder.init(cb)
cb.console_output = True
cb.output_file = "_customer.py"
cb.field_list = [
    "first_name",
    "last_name",
    "address",
    "city",
    "state",
    "zip"]

cb = ClassBuilder.create_class(cb)