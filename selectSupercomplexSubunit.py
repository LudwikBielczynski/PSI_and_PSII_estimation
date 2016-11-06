def selectSupercomplexSubunit(self):
    supercomplex_choice = self.SUPERCOMPLEX_CHOICE.get("active")
    supercomplex_subunit_choice = self.SUPERCOMPLEX_SUBUNIT_CHOICE.get("active")
    if (supercomplex_choice == "PSII") & (supercomplex_subunit_choice == "Core"):
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.delete(0, "end")
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.insert(0, self.LEAF.thylakoidMembrane.PSII.Core.N_Chl_a)
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.delete(0, "end") 
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.insert(0, self.LEAF.thylakoidMembrane.PSII.Core.N_Chl_b) 

    if (supercomplex_choice == "PSII") & (supercomplex_subunit_choice == "LHCII"):
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.delete(0, "end")
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.insert(0, self.LEAF.thylakoidMembrane.PSII.LHCII.N_Chl_a)
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.delete(0, "end") 
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.insert(0, self.LEAF.thylakoidMembrane.PSII.LHCII.N_Chl_b)    

    if (supercomplex_choice == "PSII") & (supercomplex_subunit_choice == "CP24"):
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.delete(0, "end")
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.insert(0, self.LEAF.thylakoidMembrane.PSII.minors.CP24.N_Chl_a)
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.delete(0, "end") 
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.insert(0, self.LEAF.thylakoidMembrane.PSII.minors.CP24.N_Chl_b)   

    if (supercomplex_choice == "PSII") & (supercomplex_subunit_choice == "CP26"):
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.delete(0, "end")
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.insert(0, self.LEAF.thylakoidMembrane.PSII.minors.CP26.N_Chl_a)
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.delete(0, "end") 
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.insert(0, self.LEAF.thylakoidMembrane.PSII.minors.CP26.N_Chl_b)   

    if (supercomplex_choice == "PSII") & (supercomplex_subunit_choice == "CP29"):
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.delete(0, "end")
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.insert(0, self.LEAF.thylakoidMembrane.PSII.minors.CP29.N_Chl_a)
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.delete(0, "end") 
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.insert(0, self.LEAF.thylakoidMembrane.PSII.minors.CP29.N_Chl_b)

    if (supercomplex_choice == "PSI") & (supercomplex_subunit_choice == "Core"):
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.delete(0, "end")
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.insert(0, self.LEAF.thylakoidMembrane.PSI.Core.N_Chl_a)
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.delete(0, "end") 
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.insert(0, self.LEAF.thylakoidMembrane.PSI.Core.N_Chl_b) 

    if (supercomplex_choice == "PSI") & (supercomplex_subunit_choice == "Lhca1"):
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.delete(0, "end")
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.insert(0, self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca1.N_Chl_a)
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.delete(0, "end") 
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.insert(0, self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca1.N_Chl_b) 

    if (supercomplex_choice == "PSI") & (supercomplex_subunit_choice == "Lhca2"):
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.delete(0, "end")
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.insert(0, self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca2.N_Chl_a)
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.delete(0, "end") 
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.insert(0, self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca2.N_Chl_b) 

    if (supercomplex_choice == "PSI") & (supercomplex_subunit_choice == "Lhca3"):
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.delete(0, "end")
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.insert(0, self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca3.N_Chl_a)
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.delete(0, "end") 
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.insert(0, self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca3.N_Chl_b) 

    if (supercomplex_choice == "PSI") & (supercomplex_subunit_choice == "Lhca4"):
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.delete(0, "end")
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chla_ENTRY.insert(0, self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca4.N_Chl_a)
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.delete(0, "end") 
        self.SUPERCOMPLEX_SUBUNIT_STRUCTURE_Chlb_ENTRY.insert(0, self.LEAF.thylakoidMembrane.PSI.LHCI.Lhca4.N_Chl_b) 