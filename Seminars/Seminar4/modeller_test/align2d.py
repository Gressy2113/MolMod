from modeller import *

env = Environ()
env.io.atom_files_directory = ['.', './atom_files']
aln = Alignment(env)
mdl = Model(env, file='6OO3', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='6OO3', atom_files='6OO3.pdb')
aln.append(file='MtDH.ali', align_codes='MtDH')
aln.align2d(max_gap_length=50)
aln.write(file='MtDH-6OO3.ali', alignment_format='PIR')
aln.write(file='MtDH-6OO3.pap', alignment_format='PAP')