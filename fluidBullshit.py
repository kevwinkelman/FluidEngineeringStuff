class WarmerFluidProperties:
    def __init__(self, m_w, p, k_f, v, capT1, sigma, capPR):
        self.m_w = m_w
        self.p = p
        self.k_f = k_f
        self.v = v
        self.capT1 = capT1
        self.sigma = sigma
        self.capPR = capPR


class ColderFluidProperties:
    def __init__(self, m_c, p, k_f, v, capt1, sigma, capPR):
        self.m_c = m_c
        self.p = p
        self.k_f = k_f
        self.v = v
        self.capt1 = capt1
        self.sigma = sigma
        self.capPR = capPR


#C Shell Data
class TubingSizes:
    def __init__(self, capID_t, capN_t, capOD_t, capN_p):
        self.capID_t = capID_t
        self.capN_t = capN_t
        self.capOD_t = capOD_t
        self.capN_p = capN_p


class ShellData:
    def __init__(self, capD_S, capB, capN_b, capP_t):
        self.capD_S = capD_S
        self.capB = capB
        self.capN_b = capN_b
        self.capP_t = capP_t


def warmer_fluid_input():
    warmerProperties.m_w = input("warm m_w: ")
    warmerProperties.p = input("warm p: ")
    warmerProperties.k_f = input("warm k_f: ")
    warmerProperties.v = input("warm v: ")
    warmerProperties.capT1 = input("warm capT1: ")
    warmerProperties.sigma = input("warm sigma: ")
    warmerProperties.capPR = input("warm capPR: ")

    return warmerProperties.m_w, warmerProperties.p, warmerProperties.k_f, warmerProperties.v, warmerProperties.sigma, warmerProperties.capPR

def cooler_fluid_input():
    ColderFluidProperties.m_c = input("cold m_c: ")
    ColderFluidProperties.p = input("cold p: ")
    ColderFluidProperties.k_f = input("cold k_f: ")
    ColderFluidProperties.v = input("cold v: ")
    ColderFluidProperties.capt1 = input("cold capt1: ")
    ColderFluidProperties.sigma = input("cold sigma: ")
    ColderFluidProperties.capPR = input("cold capPR: ")

    return ColderFluidProperties.m_w, ColderFluidProperties.p, ColderFluidProperties.k_f, ColderFluidProperties.v, ColderFluidProperties.sigma, ColderFluidProperties.capPR


warmerProperties = WarmerFluidProperties(0, 0, 0, 0, 0, 0, 0)
colderProperties = ColderFluidProperties(0, 0, 0, 0, 0, 0, 0)

warmer_fluid_input()
cooler_fluid_input()

print(warmerProperties.m_w, warmerProperties.p, warmerProperties.k_f, warmerProperties.v, warmerProperties.sigma, warmerProperties.capPR)