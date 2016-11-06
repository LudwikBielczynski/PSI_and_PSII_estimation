class pigmentProtein(object):
    """
    Representation of a Photosystem particle
    """   
    def __init__(self):
        """
        Initialize a PS instance, saves all parameters as attributes of the instance.
        
        Input values:
        Values calculated:
        """
        self.N_Chls = 0
        self.N_Chl_a = 0
        self.N_Chl_b = 0
        self.type = "none"


class Lhca1(pigmentProtein):
    def __init__(self, n = 1):
        self.type = "Lhca1"
        self.n = n
        self.N_Chl_a = 12*self.n
        self.N_Chl_b = 3*self.n
        self.N_Chls = self.N_Chl_a + self.N_Chl_b

class Lhca2(pigmentProtein):
    def __init__(self, n = 1):
        self.type = "Lhca2"
        self.n = n
        self.N_Chl_a = 9.6*self.n
        self.N_Chl_b = 4.2*self.n
        self.N_Chls = self.N_Chl_a + self.N_Chl_b

class Lhca3(pigmentProtein):
    def __init__(self, n = 1):
        self.type = "Lhca3"
        self.n = n
        self.N_Chl_a = 13.6*self.n
        self.N_Chl_b = 3.4*self.n
        self.N_Chls = self.N_Chl_a + self.N_Chl_b

class Lhca4(pigmentProtein):
    def __init__(self, n = 1):
        self.type = "Lhca4"
        self.n = n
        self.N_Chl_a = 10.5*self.n
        self.N_Chl_b = 4.5*self.n
        self.N_Chls = self.N_Chl_a + self.N_Chl_b

class LHCI(pigmentProtein):
    def __init__(self, n_Lhca1 = 1, n_Lhca2 = 1, n_Lhca3 = 1, n_Lhca4 = 1):
        self.type = "LHCI"
        self.Lhca1 = Lhca1(n_Lhca1)
        self.Lhca2 = Lhca2(n_Lhca2)
        self.Lhca3 = Lhca3(n_Lhca3)
        self.Lhca4 = Lhca3(n_Lhca4)        

        self.N_Chl_a = self.Lhca1.N_Chl_a + self.Lhca2.N_Chl_a + self.Lhca3.N_Chl_a + self.Lhca4.N_Chl_a
        self.N_Chl_b = self.Lhca1.N_Chl_b + self.Lhca2.N_Chl_b + self.Lhca3.N_Chl_b + self.Lhca4.N_Chl_b   

class PSI_Core(pigmentProtein):
    def __init__(self):
        self.type = "PSI_Core"
        self.N_Chl_a = 112
        self.N_Chl_b = 0
        self.N_Chls = self.N_Chl_a + self.N_Chl_b
#        self.N_Chls = 173
#        Chl_a_b_PSI = 9.7
#        self.N_Chl_b = self.N_Chls/(Chl_a_b_PSI+1)
#        self.N_Chl_a = self.N_Chls - self.N_Chl_b

class PSI(pigmentProtein):
    def __init__(self, f_full = 1):
        self.type = "PSI"
        self.Core = PSI_Core()

        self.f_full = f_full
        self.f_core = 1 - self.f_full

        self.LHCI = LHCI(n_Lhca1 = 1, n_Lhca2 = 1, n_Lhca3 = 1, n_Lhca4 = 1)

        self.N_Chl_a = (self.Core.N_Chl_a + self.LHCI.N_Chl_a)*self.f_full + self.Core.N_Chl_a*self.f_core
        self.N_Chl_b = self.LHCI.N_Chl_b*self.f_full
        self.N_Chls = self.N_Chl_a + self.N_Chl_b

    def updatePSI(self):
        self.N_Chl_a = (self.Core.N_Chl_a + self.LHCI.N_Chl_a)*self.f_full + self.Core.N_Chl_a*self.f_core
        self.N_Chl_b = self.LHCI.N_Chl_b*self.f_full
        self.N_Chls = self.N_Chl_a + self.N_Chl_b

    def updateLHCI(self):
        self.LHCI.N_Chl_a = self.LHCI.Lhca1.N_Chl_a + self.LHCI.Lhca2.N_Chl_a + self.LHCI.Lhca3.N_Chl_a + self.LHCI.Lhca4.N_Chl_a
        self.LHCI.N_Chl_b = self.LHCI.Lhca1.N_Chl_b + self.LHCI.Lhca2.N_Chl_b + self.LHCI.Lhca3.N_Chl_b + self.LHCI.Lhca4.N_Chl_b   
        self.updatePSI()


class CP24(pigmentProtein):
    def __init__(self, n = 1):
        self.type = "CP24"
        self.n = n
        self.N_Chl_a = 5
        self.N_Chl_b = 5
        self.N_Chls = self.N_Chl_a + self.N_Chl_b

class CP26(pigmentProtein):
    def __init__(self, n = 1):
        self.type = "CP26"
        self.n = n        
        self.N_Chl_a = 8
        self.N_Chl_b = 4
        self.N_Chls = self.N_Chl_a + self.N_Chl_b

class CP29(pigmentProtein):
    def __init__(self, n = 1):
        self.type = "CP29"
        self.n = n
        self.N_Chl_a = 8
        self.N_Chl_b = 4
        self.N_Chls = self.N_Chl_a + self.N_Chl_b

class minors(pigmentProtein):
    def __init__(self, n_CP24 = 1, n_CP26 = 1, n_CP29 = 1):
        self.CP24 = CP24(n_CP24)
        self.CP26 = CP26(n_CP26)
        self.CP29 = CP29(n_CP29)

        self.n_CP24 = n_CP24
        self.n_CP26 = n_CP26        
        self.n_CP29 = n_CP29

        self.N_Chl_a = self.CP24.N_Chl_a*self.n_CP24 + self.CP26.N_Chl_a*self.n_CP26 + self.CP29.N_Chl_a*self.n_CP29
        self.N_Chl_b = self.CP24.N_Chl_b*self.n_CP24 + self.CP26.N_Chl_b*self.n_CP26 + self.CP29.N_Chl_b*self.n_CP29

class LHCII(pigmentProtein):
    def __init__(self, n = 1):
        self.type = "LHCII"
        self.n = n
#        self.N_Chl_a = 24*self.n
#        self.N_Chl_b = 18*self.n
        self.N_Chl_a = 24
        self.N_Chl_b = 18
        self.N_Chls = self.N_Chl_a + self.N_Chl_b

class PSII_Core(pigmentProtein):
    def __init__(self, n = 1):
        self.type = "PSII_Core"
        self.n = n
        self.N_Chl_a = 37
        self.N_Chl_b = 0
        self.N_Chls = self.N_Chl_a + self.N_Chl_b


class PSII(pigmentProtein):
    def __init__(self, n_Core = 1., n_CP24 = 1., n_CP26 = 1., n_CP29 = 1., n_LHCII = 2.):
        self.n_Core = n_Core
        self.Core = PSII_Core(n_Core)

        self.n_CP24 = n_CP24
        self.n_CP26 = n_CP26
        self.n_CP29 = n_CP29
        self.n_LHCII = n_LHCII

        self.LHCII = LHCII(self.n_LHCII)
        self.minors = minors(n_CP24 = self.n_CP24, n_CP26 = self.n_CP26, n_CP29 = self.n_CP29)

        self.N_Chl_a = self.Core.N_Chl_a + self.minors.N_Chl_a + self.LHCII.N_Chl_a*self.LHCII.n
        self.N_Chl_b = self.minors.N_Chl_b + self.LHCII.N_Chl_b*self.LHCII.n
        self.N_Chls = self.N_Chl_a + self.N_Chl_b


    def updateMinors(self):
        self.minors.N_Chl_a = self.minors.CP24.N_Chl_a + self.minors.CP26.N_Chl_a + self.minors.CP29.N_Chl_a
        self.minors.N_Chl_b = self.minors.CP24.N_Chl_b + self.minors.CP26.N_Chl_b + self.minors.CP29.N_Chl_b   

    def updatePSII(self):
        self.N_Chl_a = self.Core.N_Chl_a + self.minors.N_Chl_a + self.LHCII.N_Chl_a*self.LHCII.n
        self.N_Chl_b = self.minors.N_Chl_b + self.LHCII.N_Chl_b*self.LHCII.n
        self.N_Chls = self.N_Chl_a + self.N_Chl_b

class thylakoidMembrane(object):
    def __init__(self, PSI_PSII = 0.7, Chl_a_b = 3.2, PSI_f_full = 1.):
        self.PSI_PSII = PSI_PSII
        self.Chl_a_b = Chl_a_b

        self.PSI = PSI(f_full = PSI_f_full)

        self.PSII = PSII()

        self.actualize_n_LHCII(self.PSI_PSII, self.Chl_a_b)

    def updateThylakoidMembrane(self, PSI_PSII, Chl_a_b, PSI_f_full):
        self.PSI.updateLHCI()
#        self.n_LHCII = ( self.PSI_PSII*( self.PSI.N_Chl_b*self.Chl_a_b - self.PSI.N_Chl_a ) + self.PSII.minors.N_Chl_b*self.Chl_a_b - self.PSII.Core.N_Chl_a - self.PSII.minors.N_Chl_a )/( self.PSII.LHCII.N_Chl_a - self.PSII.LHCII.N_Chl_b*self.Chl_a_b )
#        self.PSII.actualize_n_LHCII(self.n_LHCII)
#        self.PSII.updatePSII()
        self.actualize_n_LHCII(PSI_PSII, Chl_a_b)

    def actualize_n_LHCII(self, PSI_PSII, Chl_a_b):
        self.PSII.updateMinors()
        self.PSII.n_LHCII = ( PSI_PSII*( self.PSI.N_Chl_b*Chl_a_b - self.PSI.N_Chl_a ) + self.PSII.minors.N_Chl_b*Chl_a_b - self.PSII.Core.N_Chl_a - self.PSII.minors.N_Chl_a )/( self.PSII.LHCII.N_Chl_a - self.PSII.LHCII.N_Chl_b*Chl_a_b )
        self.PSII.LHCII.n = self.PSII.n_LHCII 
#        self.PSII.LHCII = LHCII(self.PSII.n_LHCII)
        self.PSII.updatePSII()  
#        print self.PSII.LHCII.n
#        print self.PSII.n_LHCII

class leaf(object):
    def __init__(self, PSI_PSII = 0.7, Chl_a_b = 3.2, m_Chls_fresh = 0.862, m_investigated = 1, PSI_f_full = 1):
        self.PSI_PSII = PSI_PSII
        self.Chl_a_b = Chl_a_b
        self.PSI_f_full = PSI_f_full
        self.thylakoidMembrane = thylakoidMembrane(PSI_PSII = self.PSI_PSII, Chl_a_b = self.Chl_a_b, PSI_f_full = self.PSI_f_full)

        self.m_Chls_fresh = m_Chls_fresh*10**(-3) #g Chls/g fresh weight
        self.m_investigated = m_investigated #g

        self.m_Chls = m_Chls_fresh*m_investigated

        self.n_Chl_a = ( self.Chl_a_b*self.m_Chls )/( M_Chl_a + self.Chl_a_b*M_Chl_a )
        self.n_Chl_b = ( self.m_Chls - self.n_Chl_a*M_Chl_a )/M_Chl_b

        self.n_Chl_a = self.n_Chl_a*Avogadro_number
        self.n_Chl_b = self.n_Chl_b*Avogadro_number
        self.n_Chls = self.n_Chl_a + self.n_Chl_b

        self.n_PSII = self.n_Chls/( self.PSI_PSII*( self.thylakoidMembrane.PSI.N_Chl_a  + self.thylakoidMembrane.PSI.N_Chl_b ) + self.thylakoidMembrane.PSII.N_Chl_a  + self.thylakoidMembrane.PSII.N_Chl_b )
        self.n_PSI = self.PSI_PSII*self.n_PSII

    def updateLeaf(self, PSI_PSII, Chl_a_b, m_Chls_fresh, m_investigated, PSI_f_full):

        if (m_Chls_fresh*10**(-3)) != self.m_Chls_fresh:
            self.m_Chls_fresh = m_Chls_fresh*10**(-3) #g Chls/g fresh weight
            self.m_Chls = m_Chls_fresh*m_investigated

            self.n_Chl_a = ( self.Chl_a_b*self.m_Chls )/( M_Chl_a + self.Chl_a_b*M_Chl_a )
            self.n_Chl_b = ( self.m_Chls - self.n_Chl_a*M_Chl_a )/M_Chl_b
            self.n_Chl_a = self.n_Chl_a*Avogadro_number
            self.n_Chl_b = self.n_Chl_b*Avogadro_number
            self.n_Chls = self.n_Chl_a + self.n_Chl_b

        self.thylakoidMembrane.updateThylakoidMembrane(PSI_PSII = PSI_PSII, Chl_a_b = Chl_a_b, PSI_f_full = PSI_f_full)

        self.n_PSII = self.n_Chls/( self.PSI_PSII*( self.thylakoidMembrane.PSI.N_Chl_a  + self.thylakoidMembrane.PSI.N_Chl_b ) + self.thylakoidMembrane.PSII.N_Chl_a  + self.thylakoidMembrane.PSII.N_Chl_b )
        self.n_PSI = self.PSI_PSII*self.n_PSII

Avogadro_number = 6.022*10**23
M_Chl_a = 893.509 #g/mol
M_Chl_b = 907.49  #g/mol
#WTGL200 = leaf(PSI_PSII = 0.7, Chl_a_b = 3.235, m_Chls_fresh = 0.862, m_investigated = 1)
#WTGL600 = leaf(PSI_PSII = 0.7, Chl_a_b = 3.249, m_Chls_fresh = 0.782, m_investigated = 1)
#WTGL1800 = leaf(PSI_PSII = 0.7, Chl_a_b = 3.562, m_Chls_fresh = 0.389, m_investigated = 1)
#dLhcb2GL200 = leaf(PSI_PSII = 0.7, Chl_a_b = 4.004, m_Chls_fresh = 0.674, m_investigated = 1)
#dLhcb2GL600 = leaf(PSI_PSII = 0.56, Chl_a_b = 3.993, m_Chls_fresh = 0.564, m_investigated = 1)
#dLhcb2GL1800 = leaf(PSI_PSII = 0.49, Chl_a_b = 4.057, m_Chls_fresh = 0.393, m_investigated = 1)
#print "LHCII"
#print WTGL200.thylakoidMembrane.PSII.n_LHCII
#print WTGL600.thylakoidMembrane.PSII.n_LHCII
#print WTGL1800.thylakoidMembrane.PSII.n_LHCII
#print " "
#print dLhcb2GL200.thylakoidMembrane.PSII.n_LHCII
#print dLhcb2GL600.thylakoidMembrane.PSII.n_LHCII
#print dLhcb2GL1800.thylakoidMembrane.PSII.n_LHCII
#print "PSI"
#print WTGL200.n_PSI
#print WTGL600.n_PSI
#print WTGL1800.n_PSI
#print " "
#print dLhcb2GL200.n_PSI
#print dLhcb2GL600.n_PSI
#print dLhcb2GL1800.n_PSI
#print "PSII"
#print WTGL200.n_PSII
#print WTGL600.n_PSII
#print WTGL1800.n_PSII
#print " "
#print dLhcb2GL200.n_PSII
#print dLhcb2GL600.n_PSII
#print dLhcb2GL1800.n_PSII

