from difflib import unified_diff

title = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
File Comparer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
  
with open('tropical_fruits.txt') as file_1, open('fruits.txt') as file_2:
    lines1 = file_1.readlines()
    lines2 = file_2.readlines()

    diff = list(unified_diff(lines1, lines2, fromfile='tropical_fruits.txt', tofile='fruits.txt'))

    additions = []
    deletions = []
    common_lines = []
    unknowns = []
    hunks = []

    for line in diff:
        if line.startswith('@@'):
            hunks.append(line)
        elif line.startswith('+') and not line.startswith('+++'):
            additions.append(line)
        elif line.startswith('-') and not line.startswith('---'):
            deletions.append(line)
        elif line.startswith(' '):
            common_lines.append(line)
        elif line.startswith('?'):
            unknowns.append(line)
            
  
    with open('differences.txt', 'w') as output_file:
        output_file.write(title + '\n')

        # Write headers for the diff sections
        output_file.write("File 1: --- tropical_fruits.txt\n")
        output_file.write("File 2: +++ fruits.txt\n\n")

        # Write the hunk headers
        for hunk in hunks:
            output_file.write(hunk)
        
        # Write the changes as they appear in the diff
        if common_lines:
            output_file.write("\n\nCommon in Both Files:\n")
            for common in common_lines:
                output_file.write(common)
        
        # Write the deletions
        if deletions:
            output_file.write("\n\nUnique to File 1:\n")
            for deletion in deletions:
                output_file.write(deletion)
        
        # Write the additions
        if additions:
            output_file.write("\n\nUnique to File 2:\n")
            for addition in additions:
                output_file.write(addition)

        # Write the unknowns
        if unknowns:
            output_file.write("\n\nLine not Present in Either File:\n")
            for unknown in unknowns:
                output_file.write(unknown)
