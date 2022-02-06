# Você não precisar colocar o prefixo _m em váriaveis membros, para isso as suas classes e funções devem ser pequenas.
# E deve usar um abiente de edição que realce ou colore os variaveis membro de modo a distingu-las:

class Part:
    m_dsc: str  # Descriçaõ textual

    def __init__(self):
        self.__m_dsc = ""

    @property
    def m_dsc(self):
        return self.m_dsc

    @m_dsc.setter
    def m_dsc(self, name):
        self.m_dsc = name

# -----------------------------------------


class Part:
    description: str

    def __init__(self):
        self.__description = ""

    @property
    def description(self):
        return self.description

    @description.setter
    def description(self, description):
        self.description = description
