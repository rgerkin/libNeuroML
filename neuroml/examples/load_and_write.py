import neuroml
from neuroml import loaders

doc = loaders.NeuroMLLoader.load('./test_files/Purk2M9s.nml')
print doc

f = open('./tmp/test_load_and_write.xml','w')
doc.export(f,0)
