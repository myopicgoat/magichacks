# FOR CCA EDITING ONLY
from IPython.core.magic import (Magics, magics_class, cell_magic)
from re import sub
@magics_class
class CCAMagics(Magics):
    @cell_magic
    def write2file(self, line, cell):
        """
        Purpose:
            This magic-hack executes the current cell or writes it to a file, the twist with the original %%writefile is that it can indeed execute the cell normally based on an externally-defined switch. This is useful for continuous editing & debugging. Set notebook switch to OFF for general development and debugging, set it to ON to update all saved cells in order to sync with notebook.
        Syntax:
            %%wf2 nameOfFile.py switchVariable
        Remarks:
            this command is less safe than the original %%writefile and just overwrites pre-existing files if there were any without warnings, this is fine (and desirable) in the context for which it was designed. Also the retrieval of the switch is unsafe, again, if this is used within the context of which it was created, it should be fine.
        Author:
            thibaut@cambridgecoding, Aug16
        """
        # retrieve name of file & switch variable
        line   = line.split(" ")
        fname  = line[0]
        client = eval(line[1])
        if client=='CONTENT':
            with open(fname,'w') as f:
                cell = sub(r'#</?cca>.*(\r?\n|\z)','',cell)
                f.write(cell)
        elif client=='STUDENT':
            opentag   = "#<cca>"
            closetag  = "#</cca>"
            idx_open  = cell.find(opentag)
            idx_open  = idx_open if idx_open else 0
            if idx_open:
                # get rid of stuff pre opening tag
                cell = cell[idx_open+len(opentag):]
                # get rid of first line
                cell = cell[cell.find("\n")+1:]
                #
                lcell = len(cell)
                # find closing tag
                idx_close = cell.find(closetag)
                # get rid of previous "\n" as well if there's a closing tag (idx_close-1)
                idx_close = idx_close-1 if idx_close else lcell-1
                cell = cell[:idx_close]
            # output that
            with open(fname,'w') as f:
                f.write(cell)
        elif client=='DEV+CONTENT':
            with open(fname,'w') as f:
                cell = sub(r'#</?cca>.*(\r?\n|\z)','',cell)
                f.write(cell)
            get_ipython().run_cell(cell)
        else:
            get_ipython().run_cell(cell)

get_ipython().register_magics(CCAMagics)
