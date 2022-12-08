num_fully_cont = 0


with open('day4.txt', 'r') as file:
    pairs = file.readlines()


for pair in pairs:
    elf1, elf2 = pair.strip('\n').split(',')
    elf1_sect1, elf1_sect2 = elf1.split('-')
    elf2_sect1, elf2_sect2 = elf2.split('-')
    elf1_sect1, elf1_sect2, elf2_sect1, elf2_sect2 = \
        int(elf1_sect1), int(elf1_sect2), int(elf2_sect1), int(elf2_sect2)
    # part one
    #if elf1_sect1 >= elf2_sect1 and elf1_sect2 <= elf2_sect2:
    #    num_fully_cont += 1
    #elif elf1_sect1 <= elf2_sect1 and elf1_sect2 >= elf2_sect2:
    #    num_fully_cont += 1
    
    # part two
    #if elf1_sect1 <= elf2_sect1 and elf1_sect2 >= elf2_sect1:
    #    num_fully_cont += 1
    #elif elf1_sect1 >= elf2_sect1 and elf1_sect2 <= elf2_sect1:
    #    num_fully_cont += 1
    #elif elf2_sect1 <= elf1_sect1 and elf2_sect2 >= elf1_sect1:
    #    num_fully_cont += 1
    #elif elf2_sect1 >= elf1_sect1 and elf2_sect2 <= elf1_sect1:
    #    num_fully_cont += 1
    
    # part two, more efficient NOTE: use plus one because of range
    if range(max(elf1_sect1, elf2_sect1), min(elf1_sect2, elf2_sect2)+1):
        num_fully_cont += 1

print(num_fully_cont)
