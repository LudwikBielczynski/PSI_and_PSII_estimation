def updateStructure(self):
#    print "Entered function updateStructure"
    supercomplex_choice = self.SUPERCOMPLEX_CHOICE.get("active")
    supercomplex_subunit_choice = self.SUPERCOMPLEX_SUBUNIT_CHOICE.get("active")
    if (supercomplex_choice == "PSII") & (supercomplex_subunit_choice == "Core"):

        self.LEAF.thylakoidMembrane.PSII.Core.N_Chl_a = float(self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.get())
        self.LEAF.thylakoidMembrane.PSII.Core.N_Chl_b = float(self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.get())
        string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSII.Core.N_Chl_a)
        self.canvas_PSII.itemconfig(self.image_PSII_on_canvas_text_PSII_Core_Chl_a, text = string, font = ("Helvetica", 8))
        string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSII.Core.N_Chl_b)
        self.canvas_PSII.itemconfig(self.image_PSII_on_canvas_text_PSII_Core_Chl_b, text = string, font = ("Helvetica", 8))

        self.recalculate()

        string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSII.N_Chl_a*2)
        self.canvas_PSII.itemconfig(self.image_PSII_on_canvas_text_PSII_supercomplex_Chl_a, text = string, font = ("Helvetica", 8))
        string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSII.N_Chl_b*2)
        self.canvas_PSII.itemconfig(self.image_PSII_on_canvas_text_PSII_supercomplex_Chl_b, text = string, font = ("Helvetica", 8))


    if (supercomplex_choice == "PSII") & (supercomplex_subunit_choice == "LHCII"):
        print "Entered function LHCII"
        self.LEAF.thylakoidMembrane.PSII.LHCII.N_Chl_a = float(self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.get())
        self.LEAF.thylakoidMembrane.PSII.LHCII.N_Chl_b = float(self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.get())
        string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSII.LHCII.N_Chl_a)
        self.canvas_PSII.itemconfig(self.image_PSII_on_canvas_text_PSII_LHCII_Chl_a, text = string, font = ("Helvetica", 8))
        string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSII.LHCII.N_Chl_b)
        self.canvas_PSII.itemconfig(self.image_PSII_on_canvas_text_PSII_LHCII_Chl_b, text = string, font = ("Helvetica", 8))

        self.recalculate()

        string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSII.N_Chl_a*2)
        self.canvas_PSII.itemconfig(self.image_PSII_on_canvas_text_PSII_supercomplex_Chl_a, text = string, font = ("Helvetica", 8))
        string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSII.N_Chl_b*2)
        self.canvas_PSII.itemconfig(self.image_PSII_on_canvas_text_PSII_supercomplex_Chl_b, text = string, font = ("Helvetica", 8))



    if (supercomplex_choice == "PSII") & (supercomplex_subunit_choice == "CP24"):
        self.LEAF.thylakoidMembrane.PSII.minors.CP24.N_Chl_a = float(self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.get())
        self.LEAF.thylakoidMembrane.PSII.minors.CP24.N_Chl_b = float(self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.get())
        string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSII.minors.CP24.N_Chl_a)
        self.canvas_PSII.itemconfig(self.image_PSII_on_canvas_text_PSII_CP24_Chl_a, text = string, font = ("Helvetica", 8))
        string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSII.minors.CP24.N_Chl_b)
        self.canvas_PSII.itemconfig(self.image_PSII_on_canvas_text_PSII_CP24_Chl_b, text = string, font = ("Helvetica", 8))

        self.recalculate()

        string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSII.N_Chl_a*2)
        self.canvas_PSII.itemconfig(self.image_PSII_on_canvas_text_PSII_supercomplex_Chl_a, text = string, font = ("Helvetica", 8))
        string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSII.N_Chl_b*2)
        self.canvas_PSII.itemconfig(self.image_PSII_on_canvas_text_PSII_supercomplex_Chl_b, text = string, font = ("Helvetica", 8))


    if (supercomplex_choice == "PSII") & (supercomplex_subunit_choice == "CP26"):
        self.LEAF.thylakoidMembrane.PSII.minors.CP26.N_Chl_a = float(self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.get())
        self.LEAF.thylakoidMembrane.PSII.minors.CP26.N_Chl_b = float(self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.get())
        string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSII.minors.CP26.N_Chl_a)
        self.canvas_PSII.itemconfig(self.image_PSII_on_canvas_text_PSII_CP26_Chl_a, text = string, font = ("Helvetica", 8))
        string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSII.minors.CP26.N_Chl_b)
        self.canvas_PSII.itemconfig(self.image_PSII_on_canvas_text_PSII_CP26_Chl_b, text = string, font = ("Helvetica", 8))

        self.recalculate()

        string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSII.N_Chl_a*2)
        self.canvas_PSII.itemconfig(self.image_PSII_on_canvas_text_PSII_supercomplex_Chl_a, text = string, font = ("Helvetica", 8))
        string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSII.N_Chl_b*2)
        self.canvas_PSII.itemconfig(self.image_PSII_on_canvas_text_PSII_supercomplex_Chl_b, text = string, font = ("Helvetica", 8))



    if (supercomplex_choice == "PSII") & (supercomplex_subunit_choice == "CP29"):
        self.LEAF.thylakoidMembrane.PSII.minors.CP29.N_Chl_a = float(self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.get())
        self.LEAF.thylakoidMembrane.PSII.minors.CP29.N_Chl_b = float(self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.get())
        self.LEAF.thylakoidMembrane.PSII.minors.CP29.N_Chl_a = float(self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.get())
        self.LEAF.thylakoidMembrane.PSII.minors.CP29.N_Chl_b = float(self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.get())
        string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSII.minors.CP29.N_Chl_a)
        self.canvas_PSII.itemconfig(self.image_PSII_on_canvas_text_PSII_CP29_Chl_a, text = string, font = ("Helvetica", 8))
        string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSII.minors.CP29.N_Chl_b)
        self.canvas_PSII.itemconfig(self.image_PSII_on_canvas_text_PSII_CP29_Chl_b, text = string, font = ("Helvetica", 8))

        self.recalculate()

        string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSII.N_Chl_a*2)
        self.canvas_PSII.itemconfig(self.image_PSII_on_canvas_text_PSII_supercomplex_Chl_a, text = string, font = ("Helvetica", 8))
        string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSII.N_Chl_b*2)
        self.canvas_PSII.itemconfig(self.image_PSII_on_canvas_text_PSII_supercomplex_Chl_b, text = string, font = ("Helvetica", 8))


    if (supercomplex_choice == "PSI") & (supercomplex_subunit_choice == "Core"):
        self.LEAF.thylakoidMembrane.PSI.Core.N_Chl_a = float(self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.get())
        self.LEAF.thylakoidMembrane.PSI.Core.N_Chl_b = float(self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.get())
        string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSI.Core.N_Chl_a)
        self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Core_Chl_a, text = string, font = ("Helvetica", 8))
        string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSI.Core.N_Chl_b)
        self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Core_Chl_b, text = string, font = ("Helvetica", 8))

        self.recalculate()

        string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSI.N_Chl_a)
        self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_supercomplex_Chl_a, text = string, font = ("Helvetica", 8))
        string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSI.N_Chl_b)
        self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_supercomplex_Chl_b, text = string, font = ("Helvetica", 8))




    if (supercomplex_choice == "PSI") & (supercomplex_subunit_choice == "Lhca1"):
        self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca1.N_Chl_a = float(self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.get())
        self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca1.N_Chl_b = float(self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.get())
        string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca1.N_Chl_a)
        self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Lhca1_Chl_a, text = string, font = ("Helvetica", 8))
        string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca1.N_Chl_b)
        self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Lhca1_Chl_b, text = string, font = ("Helvetica", 8))

        self.recalculate()

        string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSI.N_Chl_a)
        self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_supercomplex_Chl_a, text = string, font = ("Helvetica", 8))
        string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSI.N_Chl_b)
        self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_supercomplex_Chl_b, text = string, font = ("Helvetica", 8))



    if (supercomplex_choice == "PSI") & (supercomplex_subunit_choice == "Lhca2"):
        self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca2.N_Chl_a = float(self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.get())
        self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca2.N_Chl_b = float(self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.get())
        string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca2.N_Chl_a)
        self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Lhca2_Chl_a, text = string, font = ("Helvetica", 8))
        string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca2.N_Chl_b)
        self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Lhca2_Chl_b, text = string, font = ("Helvetica", 8))

        self.recalculate()

        string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSI.N_Chl_a)
        self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_supercomplex_Chl_a, text = string, font = ("Helvetica", 8))
        string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSI.N_Chl_b)
        self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_supercomplex_Chl_b, text = string, font = ("Helvetica", 8))

    if (supercomplex_choice == "PSI") & (supercomplex_subunit_choice == "Lhca3"):
        self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca3.N_Chl_a = float(self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.get())
        self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca3.N_Chl_b = float(self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.get())
        string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca3.N_Chl_a)
        self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Lhca3_Chl_a, text = string, font = ("Helvetica", 8))
        string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca3.N_Chl_b)
        self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Lhca3_Chl_b, text = string, font = ("Helvetica", 8))

        self.recalculate()

        string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSI.N_Chl_a)
        self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_supercomplex_Chl_a, text = string, font = ("Helvetica", 8))
        string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSI.N_Chl_b)
        self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_supercomplex_Chl_b, text = string, font = ("Helvetica", 8))

    if (supercomplex_choice == "PSI") & (supercomplex_subunit_choice == "Lhca4"):
        self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca4.N_Chl_a = float(self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.get())
        self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca4.N_Chl_b = float(self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.get())
        string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca4.N_Chl_a)
        self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Lhca4_Chl_a, text = string, font = ("Helvetica", 8))
        string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca4.N_Chl_b)
        self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_Lhca4_Chl_b, text = string, font = ("Helvetica", 8))

        self.recalculate()

        string = "Chl a: %.0f" % (self.LEAF.thylakoidMembrane.PSI.N_Chl_a)
        self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_supercomplex_Chl_a, text = string, font = ("Helvetica", 8))
        string = "Chl b: %.0f" % (self.LEAF.thylakoidMembrane.PSI.N_Chl_b)
        self.canvas_PSI.itemconfig(self.image_PSI_on_canvas_text_PSI_supercomplex_Chl_b, text = string, font = ("Helvetica", 8))
