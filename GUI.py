from Tkinter import *  
from PIL import Image, ImageDraw, ImageFont     #basic image analysis fuctions, drawing fuctions and font manipulation        
import ImageTk
from decimal import *
import sys
PROJECT_PATH = '/home/ludwik/Documents/PhDthesis/Others/Antenna size estimation/Calculations/PSIandPSIIestimation/'
sys.path.insert(0, PROJECT_PATH) # or: sys.path.insert(0, os.getcwd())
from PSIandPSIIestimation import *
from PSIIlabels import *
from PSIlabels import *
from selectSupercomplexSubunit import *
from updateStructure import *

PSI_NAME = 'PSIdescribed_empty.jpeg'
PSII_NAME = 'PSIIdescribed_empty.jpeg'


class App:
    def __init__(self, master):
 
        self.frame_input = Frame(master, width = 10, height = 600)
#        self.Title = Label(self.frame, height = 6, fg = "black", text = '\nEliminate the background by setting thresholds on HSV (Hue, Saturation and Value) channels. \n')
#        self.Instructions = Label(self.frame_input, height = 6, fg = "black", justify = LEFT, text = 'Input the values of PSI/PSII and Chl a/b ratios')

        self.CALCULATIONS_LABEL = Label(self.frame_input, text = "Calculations", height = 1, fg = "black", font = ("Helvetica", 16))
         
        entry_size = 10
        self.Chl_a_b_LABEL = Label(self.frame_input, text = "Chl a/b ratio", height = 1, fg = "black")
        self.Chl_a_b_ENTRY = Entry(self.frame_input, bg = "red", fg = "white", width = entry_size)
        self.Chl_a_b_ENTRY.insert(0, 3.235)

        self.PSI_PSII_LABEL = Label(self.frame_input, text = "PSI/PSII ratio", height = 1, fg = "black")
        self.PSI_PSII = Entry(self.frame_input, bg = "red", fg = "white", width = entry_size)
        self.PSI_PSII.insert(0, 0.7)

        self.total_Chls_LABEL = Label(self.frame_input, text = "Total Chls per fresh weight", height = 1, fg = "black")
        self.total_Chls = Entry(self.frame_input, bg = "red", fg = "white", width = entry_size)
        self.total_Chls.insert(0, 0.862)


        self.n_LHCII_LABEL = Label(self.frame_input, text = "Number of LHCII", height = 1, fg = "black")
        #Avogadro_number = 6.022*10**23
        self.LEAF = leaf(PSI_PSII = 0.7, Chl_a_b = 3.235, m_Chls_fresh = 0.862, m_investigated = 1)
        self.n_LHCII = Text(self.frame_input, height = 1, bg = "green", fg = "white", width = entry_size)
        self.n_LHCII.insert(INSERT, "%.4f" % self.LEAF.thylakoidMembrane.PSII.n_LHCII)

        self.n_PSII_LABEL = Label(self.frame_input, text = "Number of PSII RCs", height = 1, fg = "black")
        self.n_PSII = Text(self.frame_input, height = 1, bg = "green", fg = "white", width = entry_size/2)
        self.n_PSII.insert(INSERT, "{:.4E}".format(Decimal(self.LEAF.n_PSII)))

        self.n_PSI_LABEL = Label(self.frame_input, text = "Number of PSI RCs", height = 1, fg = "black")
        self.n_PSI = Text(self.frame_input, height = 1, bg = "green", fg = "white", width = entry_size/2)
        self.n_PSI.insert(INSERT, "{:.4E}".format(Decimal(self.LEAF.n_PSI)))


        self.CALCULATE_BUTTON = Button(self.frame_input, text="Recalculate", command = self.recalculate)
#        self.QUIT_BUTTON = Button(self.frame, text="Quit", command=self.frame.quit)

        self.frame = Frame(master, width = 1600, height = 600)

        self.PSI_LABEL = Label(self.frame, text = "Structure of PSI", height = 1, fg = "black", font = ("Helvetica", 16))
        self.PSII_LABEL = Label(self.frame, text = "Structure of PSII", height = 1, fg = "black", font = ("Helvetica", 16))

#        self.PSII_full_LABEL = Label(self.frame, text = "PSII supercomplex", height = 1, fg = "black", font = ("Helvetica", 8))

        self.IMAGE_PSI = Image.open(PROJECT_PATH + PSI_NAME)
        self.IMAGE_PSII = Image.open(PROJECT_PATH + PSII_NAME)
#        self.IMAGE_PSI = delete_alpha(self.IMAGE_PSI)   

        self.BASE_WIDTH = 800
        PERCENT_WIDTH = (self.BASE_WIDTH/float(self.IMAGE_PSI.size[0]))
        HEIGHT = int((float(self.IMAGE_PSI.size[1])*float(PERCENT_WIDTH)))
        self.IMAGE_PSI = self.IMAGE_PSI.resize((self.BASE_WIDTH, HEIGHT))
        self.IMAGE_PSI_ORIGINAL = self.IMAGE_PSI.copy()
        self.canvas_PSI = Canvas(self.frame, width =  self.BASE_WIDTH, height = self.BASE_WIDTH)    
        self.image_PSI = ImageTk.PhotoImage(self.IMAGE_PSI)            
        self.image_PSI_on_canvas = self.canvas_PSI.create_image(0, 0, image = self.image_PSI, anchor = NW)

        PERCENT_WIDTH = (self.BASE_WIDTH/float(self.IMAGE_PSII.size[0]))
        HEIGHT = int((float(self.IMAGE_PSII.size[1])*float(PERCENT_WIDTH)))
        self.IMAGE_PSII = self.IMAGE_PSII.resize((self.BASE_WIDTH, HEIGHT))
        self.IMAGE_PSII_ORIGINAL = self.IMAGE_PSII.copy()
        self.canvas_PSII = Canvas(self.frame, width =  self.BASE_WIDTH, height = self.BASE_WIDTH)    
        self.image_PSII = ImageTk.PhotoImage(self.IMAGE_PSII)            
        self.image_PSII_on_canvas = self.canvas_PSII.create_image(0, 0, image = self.image_PSII, anchor = NW)

        PSIIlabels(self)
        PSIlabels(self)

        self.frame_structure = Frame(master, width = 5, height = 600)


        self.SUPERCOMPLEX_STRUCTURE_LABEL = Label(self.frame_structure, text = "Structure", height = 1, fg = "black", font = ("Helvetica", 16))
        self.SUPERCOMPLEX_CHOICE_LABEL = Label(self.frame_structure, text = "Photosystem", height = 1, fg = "black")
        self.SUPERCOMPLEX_CHOICE = Listbox(self.frame_structure, height = 2, exportselection = False)
        for photosystem in ["PSII", "PSI"]:
            self.SUPERCOMPLEX_CHOICE.insert(END, photosystem)

        self.SUPERCOMPLEX_STRUCTURE = {"PSII" : ("Core", "LHCII", "CP24", "CP26", "CP29"), "PSI" : ("Core", "Lhca1", "Lhca2", "Lhca3", "Lhca4")}
        self.SUPERCOMPLEX_CHOICE_BUTTON = Button(self.frame_structure, text="Select", command = self.selectSupercomplex)

        self.SUPERCOMPLEX_SUBUNIT_CHOICE_LABEL = Label(self.frame_structure, text = "Subunit", height = 1, fg = "black")
        subunitList = self.SUPERCOMPLEX_STRUCTURE[self.SUPERCOMPLEX_CHOICE.get(ACTIVE)]
        self.SUPERCOMPLEX_SUBUNIT_CHOICE = Listbox(self.frame_structure, height = len(subunitList), exportselection = False)
        for subunit in subunitList:
            self.SUPERCOMPLEX_SUBUNIT_CHOICE.insert(END, subunit)


        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_LABEL = Label(self.frame_structure, text = "Chl a:", height = 1, fg = "black", font = ("Helvetica", 12))
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_LABEL = Label(self.frame_structure, text = "Chl b:", height = 1, fg = "black", font = ("Helvetica", 12))

        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY = Entry(self.frame_structure, bg = "red", fg = "white", width = entry_size)
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.insert(0, 0.0)

        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY = Entry(self.frame_structure, bg = "red", fg = "white", width = entry_size)
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.insert(0, 0.0)

        self.SUPERCOMPLEX_SUBUNIT_CHOICE_BUTTON = Button(self.frame_structure, text="Select", command = lambda:selectSupercomplexSubunit(self))
#        self.SUPERCOMPLEX_SUBUNIT_CHOICE_BUTTON = Button(self.frame_structure, text="Select", command = self.selectSupercomplexSubunit)

        self.UPDATE_STRUCTURE_BUTTON = Button(self.frame_structure, text="Update structures", command = lambda:updateStructure(self))


        self.initUI()

    def initUI(self):   
#        self.Title.grid(row=1,columnspan = 3, column = 2)
        self.frame_structure.pack(side = BOTTOM, expand = False) 
        self.SUPERCOMPLEX_STRUCTURE_LABEL.grid(column = 1, row = 1, columnspan = 5, rowspan = 1, sticky = W+E+S+N, pady = (0,0))
        self.SUPERCOMPLEX_CHOICE_LABEL.grid(column = 1, row = 2, columnspan = 1, rowspan = 1, sticky = W+E+S+N, pady = (0,0))
        self.SUPERCOMPLEX_CHOICE.grid(column = 1, row = 3, columnspan = 1, rowspan = 2, sticky = W+E+S+N, pady = (0,0))
        self.SUPERCOMPLEX_CHOICE_BUTTON.grid(column = 1, row = 5, columnspan = 1, rowspan = 1, sticky = W+E+S+N, pady = (0,0))

        self.SUPERCOMPLEX_SUBUNIT_CHOICE_LABEL.grid(column = 2, row = 2, columnspan = 1, rowspan = 1, sticky = W+E+S+N, pady = (0,0))
        self.SUPERCOMPLEX_SUBUNIT_CHOICE.grid(column = 2, row = 3, columnspan = 1, rowspan = 2, sticky = W+E+S+N, pady = (0,0))
        self.SUPERCOMPLEX_SUBUNIT_CHOICE_BUTTON.grid(column = 2, row = 5, columnspan = 1, rowspan = 1, sticky = W+E+S+N, pady = (0,0))

        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_LABEL.grid(column = 3, row = 3, columnspan = 1, rowspan = 1, sticky = W+E+S+N, pady = (0,0))
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_LABEL.grid(column = 3, row = 4, columnspan = 1, rowspan = 1, sticky = W+E+S+N, pady = (0,0))

        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.grid(column = 4, row = 3, columnspan = 1, rowspan = 1, sticky = W+E+S+N, pady = (0,0))
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.grid(column = 4, row = 4, columnspan = 1, rowspan = 1, sticky = W+E+S+N, pady = (0,0))

        self.UPDATE_STRUCTURE_BUTTON.grid(column = 5, row = 3, columnspan = 1, rowspan = 2, sticky = W+E+S+N, pady = (0,0))

        self.frame.pack(side = LEFT, expand = False) 
#        self.PSII_LABEL.grid(column = 1, row = 1, rowspan = 1)
#        self.canvas_PSII.grid(column = 1, row = 2, rowspan = 1)
        
#        self.canvas_PSI.grid(column = 2, row = 2, rowspan = 1)
#        self.PSI_LABEL.grid(column = 2, row = 1, rowspan = 1)

        self.PSII_LABEL.place(x = self.BASE_WIDTH/2-50, y = 0)
        self.canvas_PSII.place(x = 0, y = 40)

        self.PSI_LABEL.place(x = self.BASE_WIDTH*3/2-50, y = 0)
        self.canvas_PSI.place(x = self.BASE_WIDTH, y = 40)

        self.frame_input.pack(side = LEFT, expand = False, fill = Y)
#        self.Instructions.grid(row=2,rowspan=1,column=3, sticky=W+E+S+N,pady=(0,0))

        self.CALCULATIONS_LABEL.grid(column = 1, row = 1, columnspan = 2, rowspan = 1, sticky = W+E+S+N, pady = (0,0)) 
        self.Chl_a_b_LABEL.grid(column = 1, row = 2, columnspan = 2, rowspan = 1, sticky = W+E+S+N, pady = (0,0))
        self.Chl_a_b_ENTRY.grid(column = 1, row = 3, columnspan = 2, rowspan = 1, sticky = W+E+S+N, pady = (0,0))

        self.PSI_PSII_LABEL.grid(column = 1, row = 4, columnspan = 2, rowspan = 1, sticky = W+E+S+N, pady = (0,0))
        self.PSI_PSII.grid(column = 1, row = 5, columnspan = 2, rowspan = 1, sticky = W+E+S+N, pady=(0,0))

        self.total_Chls_LABEL.grid(column = 1, row = 6, columnspan = 2, rowspan = 1, sticky = W+E+S+N, pady = (0,0))
        self.total_Chls.grid(column = 1, row = 7, columnspan = 2, rowspan = 1, sticky = W+E+S+N, pady=(0,0))

        self.n_LHCII_LABEL.grid(column = 1, row = 9, columnspan = 2, rowspan = 1, sticky = W+E+S+N, pady = (0,0))
        self.n_LHCII.grid(column = 1, row = 10, columnspan = 2, rowspan = 1, sticky = W+E+S+N, pady = (0,0))

        self.n_PSI_LABEL.grid(column = 1, row = 11, columnspan = 1, rowspan = 1, sticky = W+E+S+N, pady = (0,0))
        self.n_PSI.grid(column = 1, row = 12, columnspan = 1, rowspan = 1, sticky = W+E+S+N, pady = (0,0))

        self.n_PSII_LABEL.grid(column = 2, row = 11, columnspan = 1, rowspan = 1, sticky = W+E+S+N, pady = (0,0))
        self.n_PSII.grid(column = 2, row = 12, columnspan = 1, rowspan = 1, sticky = W+E+S+N, pady = (0,0))

        self.CALCULATE_BUTTON.grid(column = 1, row = 13, columnspan = 2, rowspan = 1, sticky = W+E+S+N, pady = (0,0))

#        self.QUIT_BUTTON.grid(row=10,rowspan=1,column=3, sticky=W+E+S+N,pady=(0,0))

    def recalculate(self):
        new_Chl_a_b = self.Chl_a_b_ENTRY.get()
        new_PSI_PSII = self.PSI_PSII.get()
        new_total_Chls = self.total_Chls.get()
#        self.LEAF = leaf(PSI_PSII = float(new_PSI_PSII), Chl_a_b = float(new_Chl_a_b), m_Chls_fresh = float(new_total_Chls), m_investigated = 1)
        self.LEAF.updateLeaf(PSI_PSII = float(new_PSI_PSII), Chl_a_b = float(new_Chl_a_b), m_Chls_fresh = float(new_total_Chls), m_investigated = 1, PSI_f_full = 1)
        self.n_LHCII.delete(1.0, INSERT)
        self.n_LHCII.insert(INSERT, "%.4f" % self.LEAF.thylakoidMembrane.PSII.n_LHCII)

        string = "n: %.3f" % (self.LEAF.thylakoidMembrane.PSII.n_LHCII)
        self.canvas_PSII.itemconfig(self.image_PSII_on_canvas_text_PSII_n_LHCII, text = string, font = ("Helvetica", 8))

        self.n_PSII.delete(1.0, INSERT)
        self.n_PSII.insert(INSERT, "{:.4E}".format(Decimal(self.LEAF.n_PSII)))

        self.n_PSI.delete(1.0, INSERT)
        self.n_PSI.insert(INSERT, "{:.4E}".format(Decimal(self.LEAF.n_PSI)))

    def selectSupercomplex(self):
        subunitList = self.SUPERCOMPLEX_STRUCTURE[self.SUPERCOMPLEX_CHOICE.get(ACTIVE)]
        self.SUPERCOMPLEX_SUBUNIT_CHOICE.delete(0, END)
        for subunit in subunitList:
            self.SUPERCOMPLEX_SUBUNIT_CHOICE.insert(END, subunit)

Avogadro_number = 6.022*10**23
M_Chl_a = 893.509 #g/mol
M_Chl_b = 907.49  #g/mol

def main():
    root = Tk()
    root.configure(background='white')
    root.title("LHCII antenna size")
    root.option_add("*background", "white")
    app = App(root)

    root.mainloop()
 #   root.destroy()

main()