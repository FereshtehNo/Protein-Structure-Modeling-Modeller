from modeller import *
from modeller.automodel import *

# Create a Modeller environment
env = Environ()

# Set various parameters
env.io.atom_files_directory = 'D:\Research-All\Laccase\modeller'
env.io.output_directory = 'D:\Research-All\Laccase\modeller'
env.io.hetatm = True
env.io.water = True

# Create an AutoModel object
a = AutoModel(env, alnfile='alignment.ali',
              knowns='6klg', sequence='lac2',
              assess_methods=(assess.DOPE, assess.GA341))
a.starting_model = 1
a.ending_model = 20

# Set topology and library paths
env.libs.topology.read(file='$(LIB)/top.lib')
env.libs.parameters.read(file='$(LIB)/par.lib')

# Perform the homology modeling
a.make()
