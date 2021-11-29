# LED display
display = [
    """\
  #
  #
  #
  #
  #
""",
    """\
###
  #
###
#  
###
""",
    """\
###
  #
###
  #
###
""",
    """\
# #
# #
###
  #
  #
""",
    """\
###
#  
###
  #
###
""",
    """\
###
#  
###
# #
###
""",
    """\
###
  #
  #
  #
  #
""",
    """\
###
# #
###
# #
###
""",
    """\
###
# #
###
  #
###
""",
    """\
###
# #
# #
# #
###
"""
    ]
output = ""
text = input("Enter a non-negative integer number: ")
try:
    number = int(text)
    if number > 0:
        for i in range(0,20,4):
            for char in text:
                output += display[int(char) - 1][i:i+3]
                output += " "
            output += "\n"
        print(output)
    else:
        print("Please enter a non-negative number")
except:
    print("That is an invalid number. Please try again.")


