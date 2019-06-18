import math

class WarmerFluidProperties:
    def __init__(self, m_w, p, k_f, v, capT1, capC_p, alpha, capPR):
        self.m_w = m_w
        self.p = p
        self.k_f = k_f
        self.v = v
        self.capT1 = capT1
        self.capC_p = capC_p
        self.alpha = alpha
        self.capPR = capPR


class ColderFluidProperties:
    def __init__(self, m_c, p, k_f, v, capt1, capC_p, alpha, capPR):
        self.m_c = m_c
        self.p = p
        self.k_f = k_f
        self.v = v
        self.capt1 = capt1
        self.capC_p = capC_p
        self.alpha = alpha
        self.capPR = capPR


# C Shell Data
class TubingSizes:
    def __init__(self, capID_t, capN_t, capOD_t, capN_p):
        self.capID_t = capID_t
        self.capN_t = capN_t
        self.capOD_t = capOD_t
        self.capN_p = capN_p


class ShellData:
    def __init__(self, capD_S, capB, capN_b, capP_t, c):
        self.capD_S = capD_S
        self.capB = capB
        self.capN_b = capN_b
        self.capP_t = capP_t
        self.c = c

class FlowAreaData:
    def __init__(self, capA_t, capA_s):
        self.capA_t = capA_t
        self.capA_s = capA_s


class FluidVelocitiesData:
    def __init__(self, capV_t, capV_s):
        self.capV_t = capV_t
        self.capV_s = capV_s

class ShellEquivalentDiameter:
    def __init__(self, capD_eSquare, capD_eTriangle):
        self.capD_eSquare = capD_eSquare
        self.capD_eTriangle = capD_eTriangle

class ReynoldsNumbers:
    def __init__(self, capRe_t, capRe_s):
        self.capRe_t = capRe_t
        self.capRe_s = capRe_s

def warmer_fluid_input():
    warmerProperties.m_w = float(input("warm m_w: "))
    warmerProperties.p = float(input("warm p: "))
    warmerProperties.k_f = float(input("warm k_f: "))
    warmerProperties.v = float(input("warm v: "))
    warmerProperties.capT1 = float(input("warm capT1: "))
    warmerProperties.alpha = float(input("warm alpha: "))
    warmerProperties.capPR = float(input("warm capPR: "))

    return warmerProperties.m_w, warmerProperties.p, warmerProperties.k_f, warmerProperties.v, warmerProperties.alpha, warmerProperties.capPR


def cooler_fluid_input():
    colderProperties.m_c = float(input("cold m_c: "))
    colderProperties.p = float(input("cold p: "))
    colderProperties.k_f = float(input("cold k_f: "))
    colderProperties.v = float(input("cold v: "))
    colderProperties.capt1 = float(input("cold capt1: "))
    colderProperties.alpha = float(input("cold alpha: "))
    colderProperties.capPR = float(input("cold capPR: "))

    return colderProperties.m_c, colderProperties.p, colderProperties.k_f, colderProperties.v, colderProperties.alpha, colderProperties.capPR


def tubing_sizes_input():
    TubingSizes.capID_t = float(input("capID_t: "))
    TubingSizes.capN_t = float(input("capN_t: "))
    TubingSizes.capOD_t = float(input("capOD_t: "))
    TubingSizes.capN_p = int(input("capN_p: "))

    return tubingProperties.capID_t, tubingProperties.capN_t, tubingProperties.capOD_t, tubingProperties.capN_p


def shell_input():
    ShellData.capD_S = float(input("capD_S: "))
    ShellData.capB = float(input("capB: "))
    ShellData.capN_b = int(input("capN_b: "))
    ShellData.capP_t = float(input("capP_t: "))
    ShellData.c = float(shellProperties.capP_t) - float(tubingProperties.capOD_t)

    return shellProperties.capD_S, shellProperties.capB, shellProperties.capN_b, shellProperties.capP_t, shellProperties.c


warmerProperties = WarmerFluidProperties(float(21.4), float(995), float(.625), float((7.05 * math.pow(10, -7))), float(43.3), float(4179), float((1.45 * math.pow(10, -7))), float(4.69))
colderProperties = ColderFluidProperties(float(18.88), float(62.3), float(.606), float((9.16 * math.pow(10, -7))), float(18.3), float(4181), float((1.45 * math.pow(10, -7))), float(6.32))
tubingProperties = TubingSizes(float(16.55), float(196), float(19.07), float(2))
shellProperties = ShellData(float(438.2), float(304.8), float(15), float(25.4), float(6.33))
flowData = FlowAreaData(float(0), float(0))
fluidVelocityData = FluidVelocitiesData (float(0), float(0))
shellEquivalentDiameterData = ShellEquivalentDiameter(float(0), float(0))
reynoldsNumbersData = ReynoldsNumbers(float(0) , float(0))

warmer_fluid_input()
cooler_fluid_input()
tubing_sizes_input()
shell_input()

# D Flow Area's
def FlowAreasTube():
        flowData.capA_t = (float(tubingProperties.capN_t) * math.pi * math.pow(tubingProperties.capID_t, 2)) / (4 * tubingProperties.capN_p)
        return flowData.capA_t

def FlowAreasShell():
        flowData.capA_s = (shellProperties.capD_S * shellProperties.c * float(shellProperties.capB)) / shellProperties.capP_t
        return flowData.capA_s

FlowAreasTube()
FlowAreasShell()

# print(flowData.capA_t)
# print(flowData.capA_s)


# E Fluid Velocities
def FluidVelocityTube():
    fluidVelocityData.capV_t = warmerProperties.m_w / (warmerProperties.p * flowData.capA_t)
    return fluidVelocityData.capV_t

def FluidVelocityShell():
    fluidVelocityData.capV_s = colderProperties.m_c / (colderProperties.p * flowData.capA_s)
    return fluidVelocityData.capV_s

FluidVelocityTube()
FluidVelocityShell()

# print(fluidVelocityData.capV_t)
# print(fluidVelocityData.capV_s)


#F Shell Equivalent Diameter
def calculateShellEquivalentDiameterSquare():
    shellEquivalentDiameterData.capD_eSquare = (4 * (math.pow(shellProperties.capP_t, 2)) - (math.pi * math.pow(tubingProperties.capOD_t, 2))) / (math.pi * tubingProperties.capOD_t)
    return shellEquivalentDiameterData.capD_eSquare

def calculateShellEquivalentDiameterTriangle():
    shellEquivalentDiameterData.capD_eTriangle = (3.46 * (math.pow(shellProperties.capP_t, 2)) - (math.pi * math.pow(tubingProperties.capOD_t, 2))) / (math.pi * tubingProperties.capOD_t)
    return shellEquivalentDiameterData.capD_eTriangle

calculateShellEquivalentDiameterSquare()
calculateShellEquivalentDiameterTriangle()

#G Reynolds Numbers
def calculateReynoldsNumbersTube():
    reynoldsNumbersData.capRe_t = (fluidVelocityData.capV_t * tubingProperties.capID_t) / colderProperties.v
    return  reynoldsNumbersData.capRe_t
#
def calculateReynoldsNumbersShell():
    reynoldsNumbersData.capRe_s = (fluidVelocityData.capV_s * shellEquivalentDiameterData.capD_eTriangle) / warmerProperties.v
    return  reynoldsNumbersData.capRe_s

calculateReynoldsNumbersTube()
calculateReynoldsNumbersShell()

# print(reynoldsNumbersData.capRe_s)
# print(reynoldsNumbersData.capRe_t)

def writeTextFile():
    text_file = open("Results.txt", "w")
    text_file.write("Warmer Properties for Distilled Water Inputs\n")
    text_file.write("m_w: " + str(warmerProperties.m_w) + "\n")
    text_file.write("p: " + str(warmerProperties.p) + "\n")
    text_file.write("k_f: " + str(warmerProperties.k_f) + "\n")
    text_file.write("v: " + str(warmerProperties.v) + "\n")
    text_file.write("capT1: " + str(warmerProperties.capT1) + "\n")
    text_file.write("capC_p: " + str(warmerProperties.capC_p) + "\n")
    text_file.write("alpha: " + str(warmerProperties.alpha) + "\n")
    text_file.write("capPR: " + str(warmerProperties.capPR) + "\n\n")

    text_file.write("Colder Properties for Raw Water Inputs\n")
    text_file.write("m_c: " + str(colderProperties.m_c) + "\n")
    text_file.write("p: " + str(colderProperties.p) + "\n")
    text_file.write("k_f: " + str(colderProperties.k_f) + "\n")
    text_file.write("v: " + str(colderProperties.v) + "\n")
    text_file.write("capt1: " + str(colderProperties.capt1) + "\n")
    text_file.write("capC_p: " + str(colderProperties.capC_p) + "\n")
    text_file.write("alpha: " + str(colderProperties.alpha) + "\n")
    text_file.write("capPR: " + str(colderProperties.capPR) + "\n\n")

    text_file.write("Tubing Inputs\n")
    text_file.write("capID_t: " + str(tubingProperties.capID_t) + "\n")
    text_file.write("capN_t: " + str(tubingProperties.capN_t) + "\n")
    text_file.write("capOD_t: " + str(tubingProperties.capOD_t) + "\n")
    text_file.write("capN_p: " + str(tubingProperties.capN_p) + "\n\n")

    text_file.write("Shell Inputs\n")
    text_file.write("capD_S: " + str(shellProperties.capD_S) + "\n")
    text_file.write("capB: " + str(shellProperties.capB) + "\n")
    text_file.write("capN_b: " + str(shellProperties.capN_b) + "\n")
    text_file.write("capP_t: " + str(shellProperties.capP_t) + "\n")
    text_file.write("c: " + str(shellProperties.c) + "\n\n")

    text_file.write("#D Flow Area Results\n")
    text_file.write("capA_t: " + str(flowData.capA_t) + "\n")
    text_file.write("capA_s: " + str(flowData.capA_s) + "\n\n")

    text_file.write("#E Fluid Velocities Results\n")
    text_file.write("capV_t: " + str(fluidVelocityData.capV_t) + "\n")
    text_file.write("capV_s: " + str(fluidVelocityData.capV_s) + "\n\n")

    text_file.write("#F Shell Equivalent Diameter Results\n")
    text_file.write("capD_eSquare: " + str(shellEquivalentDiameterData.capD_eSquare) + "\n")
    text_file.write("capD_eTriangle: " + str(shellEquivalentDiameterData.capD_eTriangle) + "\n\n")

    text_file.write("#G Reynolds Numbers Results\n")
    text_file.write("capRe_s: " + str(reynoldsNumbersData.capRe_s) + "\n")
    text_file.write("capRe_t: " + str(reynoldsNumbersData.capRe_t) + "\n")

    text_file.close()

writeTextFile()