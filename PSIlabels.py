def PSIlabels(self):
    self.PSI_anchor_text = {"supercomplex" : (13, 365), "Core" : (357, 118), "Lhca1" : (728, 19), "Lhca2" : (594, 129), "Lhca3" : (633, 234), "Lhca4" : (536, 420)}
    space = 12
    self.image_PSI_on_canvas_text_PSI_supercomplex = self.canvas_PSI.create_text(self.PSI_anchor_text["supercomplex"][0], self.PSI_anchor_text["supercomplex"][1], anchor="nw")
    self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_supercomplex, text = "PSI supercomplex", font = ("Helvetica", 8))
    self.image_PSI_on_canvas_text_PSI_supercomplex_Chl_a = self.canvas_PSI.create_text(self.PSI_anchor_text["supercomplex"][0], self.PSI_anchor_text["supercomplex"][1] + space, anchor="nw")
    string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSI.N_Chl_a)
    self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_supercomplex_Chl_a, text = string, font = ("Helvetica", 8))
    self.image_PSI_on_canvas_text_PSI_supercomplex_Chl_b = self.canvas_PSI.create_text(self.PSI_anchor_text["supercomplex"][0], self.PSI_anchor_text["supercomplex"][1] + 2*space, anchor="nw")
    string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSI.N_Chl_b)
    self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_supercomplex_Chl_b, text = string, font = ("Helvetica", 8))

    self.image_PSI_on_canvas_text_PSI_Core = self.canvas_PSI.create_text(self.PSI_anchor_text["Core"][0], self.PSI_anchor_text["Core"][1], anchor="nw")
    self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Core, text = "Core", font = ("Helvetica", 8))
    self.image_PSI_on_canvas_text_PSI_Core_Chl_a = self.canvas_PSI.create_text(self.PSI_anchor_text["Core"][0], self.PSI_anchor_text["Core"][1] + space, anchor="nw")
    string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSI.Core.N_Chl_a)
    self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Core_Chl_a, text = string, font = ("Helvetica", 8))
    self.image_PSI_on_canvas_text_PSI_Core_Chl_b = self.canvas_PSI.create_text(self.PSI_anchor_text["Core"][0], self.PSI_anchor_text["Core"][1] + 2*space, anchor="nw")
    string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSI.Core.N_Chl_b)
    self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Core_Chl_b, text = string, font = ("Helvetica", 8))

    self.image_PSI_on_canvas_text_PSI_Lhca1 = self.canvas_PSI.create_text(self.PSI_anchor_text["Lhca1"][0], self.PSI_anchor_text["Lhca1"][1], anchor="nw")
    self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Lhca1, text = "Lhca1", font = ("Helvetica", 8))
    self.image_PSI_on_canvas_text_PSI_Lhca1_Chl_a = self.canvas_PSI.create_text(self.PSI_anchor_text["Lhca1"][0], self.PSI_anchor_text["Lhca1"][1] + space, anchor="nw")
    string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca1.N_Chl_a)
    self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Lhca1_Chl_a, text = string, font = ("Helvetica", 8))
    self.image_PSI_on_canvas_text_PSI_Lhca1_Chl_b = self.canvas_PSI.create_text(self.PSI_anchor_text["Lhca1"][0], self.PSI_anchor_text["Lhca1"][1] + 2*space, anchor="nw")
    string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca1.N_Chl_b)
    self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Lhca1_Chl_b, text = string, font = ("Helvetica", 8))

    self.image_PSI_on_canvas_text_PSI_Lhca2 = self.canvas_PSI.create_text(self.PSI_anchor_text["Lhca2"][0], self.PSI_anchor_text["Lhca2"][1], anchor="nw")
    self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Lhca2, text = "Lhca2", font = ("Helvetica", 8))
    self.image_PSI_on_canvas_text_PSI_Lhca2_Chl_a = self.canvas_PSI.create_text(self.PSI_anchor_text["Lhca2"][0], self.PSI_anchor_text["Lhca2"][1] + space, anchor="nw")
    string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca2.N_Chl_a)
    self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Lhca2_Chl_a, text = string, font = ("Helvetica", 8))
    self.image_PSI_on_canvas_text_PSI_Lhca2_Chl_b = self.canvas_PSI.create_text(self.PSI_anchor_text["Lhca2"][0], self.PSI_anchor_text["Lhca2"][1] + 2*space, anchor="nw")
    string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca2.N_Chl_b)
    self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Lhca2_Chl_b, text = string, font = ("Helvetica", 8))

    self.image_PSI_on_canvas_text_PSI_Lhca3 = self.canvas_PSI.create_text(self.PSI_anchor_text["Lhca3"][0], self.PSI_anchor_text["Lhca3"][1], anchor="nw")
    self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Lhca3, text = "Lhca3", font = ("Helvetica", 8))
    self.image_PSI_on_canvas_text_PSI_Lhca3_Chl_a = self.canvas_PSI.create_text(self.PSI_anchor_text["Lhca3"][0], self.PSI_anchor_text["Lhca3"][1] + space, anchor="nw")
    string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca3.N_Chl_a)
    self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Lhca3_Chl_a, text = string, font = ("Helvetica", 8))
    self.image_PSI_on_canvas_text_PSI_Lhca3_Chl_b = self.canvas_PSI.create_text(self.PSI_anchor_text["Lhca3"][0], self.PSI_anchor_text["Lhca3"][1] + 2*space, anchor="nw")
    string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca3.N_Chl_b)
    self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Lhca3_Chl_b, text = string, font = ("Helvetica", 8))

    self.image_PSI_on_canvas_text_PSI_Lhca4 = self.canvas_PSI.create_text(self.PSI_anchor_text["Lhca4"][0], self.PSI_anchor_text["Lhca4"][1], anchor="nw")
    self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Lhca4, text = "Lhca4", font = ("Helvetica", 8))
    self.image_PSI_on_canvas_text_PSI_Lhca4_Chl_a = self.canvas_PSI.create_text(self.PSI_anchor_text["Lhca4"][0], self.PSI_anchor_text["Lhca4"][1] + space, anchor="nw")
    string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca4.N_Chl_a)
    self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Lhca4_Chl_a, text = string, font = ("Helvetica", 8))
    self.image_PSI_on_canvas_text_PSI_Lhca4_Chl_b = self.canvas_PSI.create_text(self.PSI_anchor_text["Lhca4"][0], self.PSI_anchor_text["Lhca4"][1] + 2*space, anchor="nw")
    string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca4.N_Chl_b)
    self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Lhca4_Chl_b, text = string, font = ("Helvetica", 8))