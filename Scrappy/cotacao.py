# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options


class Cotacao:
    def __init__(self, driver):
        self.driver = driver
        self.search = "symbol_entry" # ID
        self.titulo = "inline heading" #class
        self.url = "https://br.advfn.com/bolsa-de-valores/bovespa/movida-MOVI3/cotacao"
        self.box = "quote_top" #ID
        self.tnome = "th"
        self.tcod = '//*[@id="quote_top"]/div[3]/table/tbody/tr[1]/th[2]'

    def navegacao(self):
        self.driver.get(self.url)
        try:
            element_present = EC.presence_of_element_located((By.ID, self.search))
            WebDriverWait(self.driver, 30).until(element_present)

        except TimeoutException:
            print('Elemento não encontrado')
            self.driver.close()
            self.driver.quit()

    def busca(self, acao):
        self.driver.find_element_by_id(self.search).clear()
        self.driver.find_element_by_id(self.search).send_keys(acao)
        self.driver.find_element_by_id(self.search).submit()

    def __get__area(self):
        return self.driver.find_elements_by_id(self.box)

    def __get__name(self, inf):
        return f'''{inf.find_element_by_tag_name(self.tnome).text} : {inf.find_element_by_xpath("//*[@id='quote_top']/div[3]/table/tbody/tr[2]/td[1]").text}'''

    def __get__cod(self, inf):
        return f'''{inf.find_element_by_xpath(self.tcod).text} : {inf.find_element_by_xpath('//*[@id="quote_top"]/div[3]/table/tbody/tr[2]/td[2]').text}'''

    def __get__bolsa(self,inf):
        return f'''{inf.find_element_by_xpath('//*[@id="quote_top"]/div[3]/table/tbody/tr[1]/th[3]').text} : {inf.find_element_by_xpath('//*[@id="quote_top"]/div[3]/table/tbody/tr[2]/td[3]').text}'''

    def __get__tip_arq(self,inf):
        return f'''{inf.find_element_by_xpath('//*[@id="quote_top"]/div[3]/table/tbody/tr[1]/th[4]').text} : {inf.find_element_by_xpath('//*[@id="quote_top"]/div[3]/table/tbody/tr[2]/td[4]').text}'''

    def __get__cod_ativo(self,inf):
        return f'''{inf.find_element_by_xpath('//*[@id="quote_top"]/div[3]/table/tbody/tr[1]/th[5]').text} : {inf.find_element_by_xpath('//*[@id="quote_top"]/div[3]/table/tbody/tr[2]/td[5]').text}'''

    def __get__variacao(self,inf):
        return f'''{inf.find_element_by_xpath('//*[@id="quote_top"]/div[4]/table/tbody/tr[1]/th[2]').text} : {inf.find_element_by_xpath('//*[@id="quote_top"]/div[4]/table/tbody/tr[2]/td[2]').text}'''

    def __get__ult_preco(self,inf):
        return f'''{inf.find_element_by_xpath('//*[@id="quote_top"]/div[4]/table/tbody/tr[1]/th[4]').text} : {inf.find_element_by_xpath('//*[@id="quote_top"]/div[4]/table/tbody/tr[2]/td[4]').text}'''

    def __get__preco_fechado(self,inf):
        return f'''{inf.find_element_by_xpath('//*[@id="quote_top"]/div[4]/table/tbody/tr[1]/th[8]').text} : {inf.find_element_by_xpath('//*[@id="quote_top"]/div[4]/table/tbody/tr[2]/td[8]').text}'''

    def __get__preco_compra(self,inf):
        return f'''{inf.find_element_by_xpath('//*[@id="quote_top"]/div[5]/table/tbody/tr[1]/th[1]').text} : {inf.find_element_by_xpath('//*[@id="quote_top"]/div[5]/table/tbody/tr[2]/td[1]').text}'''

    def __get__preco_venda(self,inf):
        return f'''{inf.find_element_by_xpath('//*[@id="quote_top"]/div[5]/table/tbody/tr[1]/th[2]').text} : {inf.find_element_by_xpath('//*[@id="quote_top"]/div[5]/table/tbody/tr[2]/td[2]').text}'''

    def boxes(self):
        for box in self.__get__area():
            print((self.__get__name(box),
                  self.__get__cod(box),
                  self.__get__bolsa(box),
                  self.__get__tip_arq(box),
                  self.__get__cod_ativo(box),
                  self.__get__variacao(box),
                  self.__get__ult_preco(box),
                  self.__get__preco_fechado(box),
                  self.__get__preco_compra(box),
                  self.__get__preco_venda(box)
                   ))
            print()


drivers = Options()
drivers.add_argument("--headless")
drivers.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=drivers)  # Para executar o processo sem Browser
#driver = webdriver.Chrome() # Para acompanhar o processo pelo browser

crawl = Cotacao(driver)
crawl.navegacao()
cont = 0
acao = ('petr4', 'movi3', 'IBOV11', 'VALE3', 'ITUB4',
        'BBAS3', 'BOVA11','SUZB3','BBDC4','UGPA3',
        'MGLU3','ABEV3','FIBR3','CMIG4','PETR3',
        'ITSA4','BRFS3','B3SA3','PCAR4','GGBR4','KROT3',
        'BRKM5','BTOW3','GOAU4','ESTC3','FLRY3','EGIE3',
        'USIM5','EQTL3','LREN3','BBSE3','WEGE3','KLBN11',
        'BRAP4','CIEL3','HYPE3','GOLL4','BIDI4','CCRO3',
        'VVAR11','SMLS3','CVCB3','LAME4','RADL3','RAIL3',
        'HGTX3','DMMO3','CSNA3','JBSS3','ELET3','SLCE3',
        'BRML3','IGTA3','CSAN3','QUAL3','TIMP3','EMBR3',
        'PSSA3','BBDC3','SEDU3','MRVE3','SBSP3','CRFB3',
        'MRFG3','TAEE11','MULT3','VLID3','AZUL4','IRBR3',
        'SULA11','SANB11','ELET6','BOVV11','ECOR3','CPFE3',
        'ENBR3','VIVT4','ENGI11','TRPL4','DTEX3','SAPR11',
        'CYRE3','HAPV3','BRDT3','NATU3','MYPK3','CSMG3',
        'PARD3','BRSR6','ALUP11','BEEF3','MDIA3','ALPA4',
        'AAPL34','LIGT3','COWC34','UNIP6','GFSA3','CPLE6',
        'TUPY3','CESP6','RAPT4','ITUB3','TEND3','ENEV3',
        'IVVB11','QGEP3','SMTO3','KNCR11','VULC3','ATOM3',
        'MPLU3','TGMA3','LINX3','EZTC3','ABCB4','KNRI11',
        'PRIO3','ODPV3','TIET11','FESA4','LAME3','TOTS3',
        'ARZZ3','PIBB11','LEVE3','GNDI3','SMAL11','CCPR3',
        'POMO4','SEER3','BRCR11','GUAR3','MAGG3','ANIM3',
        'STBP3','BKBR3','ALSC3','CAML3','CMIG3','HGCR11',
        'WIZS3','OMGE3','GRND3','HGLG11','AMAR3','MEAL3',
        'OIBR3','ELPL3','GBIO33','BBPO11','GOGL34','HBOR3',
        'SAPR4','FHER3','AALR3','VISC11','CGAS5','HOME34',
        'RLOG3','HGBS11','HGRE11','JNJB34','DIRR3','BRPR3',
        'KNIP11','GGRC11','TGAR11B','LCAM3','XPLG11','MSCD34',
        'AGRO3','BPAC11','MXRF11','JPMC34','SAAG11','OIBR4',
        'PTBL3','WALM34','CEBR3','LOGN3','AMZO34','HBTT11',
        'UNIP3','GGBR3','CPLE3','JSRE11','CLSC3','CARD3',
        'MSFT34','TWTR34','CMCS34','BBFI11B','BBRK3','JSLG3',
        'LIQO3','CEBR6','KLBN4','PMAM3','FIGS11','VRTA11',
        'VERZ34','BCFF11','BZLI11','UBSR11','AVON34','FBOK34',
        'TCSA3','AGCX11','MALL11','KEPL3','BCRI11','JHSF3',
        'BRIN3','FRAS3','ITSA3','VISA34','IBMB34','ROMI3',
        'FIIB11','GOGL35','SANB4','VIVR3','XPML11','OGXP3',
        'CGAS3','JPSA3','HGJH11','DAGB33','EXXO34','CRPG5',
        'VIVT3','XRXB34','TEXA34','PEPB34','EVEN3','BRAP3',
        'TBOF11','ATTB34','CSCO34','CTGP34','PDGR3','WFCO34',
        'AEFI11','HALI34','TPIS3','FAMB11B','FFCI11','CGRA4',
        'BOAC34','CESP3','SHOW3','ABCP11','EUCA4','IRDM11',
        'BERK34','GEOO34','GOAU3','CEOC11','CHVX34','PFRM3',
        'SANB3','RSID3','CPRE3','POSI3','DISB34','SHUL4',
        'ITLC34','ALMI11','XPCM11','GUAR4','PFIZ34','NIKE34',
        'INEP4','FAED11','DIVO11','SNSL3','UPAC34','CRIV3',
        'KNHY11','TIET4','FEXC11','OUJP11','CATP34','LPSB3',
        'PGCO34','RNGO11','HFOF11','MCDC34','VVAR4','UTEC34',
        'GRLV11','SAPR3','JOPA3','VTLT11','NFLX34','OFSA3',
        'GSGI34','COCA34','RBRR11','BOEI34','TMOS34','PQDP11',
        'SGPS3','ENMA3B','LIPR3','LILY34','LMTB34','VVAR3',
        'TRIS3','SCHW34','ORCL34','HTMX11','BRAX11','FJTA4',
        'LUPA3','FOFT11','FDXB34','TECN3','FVBI11','CEBR3',
        'LOGN3','AMZO34','HBTT11','UNIP3','GGBR3','CPLE3',
        'JSRE11','CLSC3','CARD3','MSFT34','TWTR34','CMCS34',
        'BBFI11B','BBRK3','JSLG3','LIQO3','CEBR6','KLBN4',
        'PMAM3','FIGS11','VRTA11','VERZ34','BCFF11','BZLI11',
        'UBSR11','AVON34','FBOK34','TCSA3','AGCX11','MALL11',
        'KEPL3','BCRI11','JHSF3','BRIN3','FRAS3','ITSA3',
        'VISA34','IBMB34','ROMI3','FIIB11','GOGL35','SANB4',
        'VIVR3','XPML11','OGXP3','CGAS3','JPSA3','HGJH11',
        'DAGB33','EXXO34','CRPG5','VIVT3','XRXB34','TEXA34',
        'PEPB34','EVEN3','BRAP3','TBOF11','ATTB34','CSCO34',
        'CTGP34','PDGR3','WFCO34','AEFI11','HALI34','TPIS3',
        'FAMB11B','FFCI11','CGRA4','BOAC34','CESP3','SHOW3',
        'ABCP11','EUCA4','IRDM11','BERK34','GEOO34','GOAU3',
        'CEOC11','CHVX34','PFRM3','SANB3','RSID3','CPRE3',
        'POSI3','DISB34','SHUL4','ITLC34','ALMI11','XPCM11',
        'GUAR4','PFIZ34','NIKE34','INEP4','FAED11','DIVO11',
        'SNSL3','UPAC34','CRIV3','KNHY11','TIET4','FEXC11',
        'OUJP11','CATP34','LPSB3','PGCO34','RNGO11','HFOF11',
        'MCDC34','VVAR4','UTEC34','GRLV11','SAPR3','JOPA3',
        'VTLT11','NFLX34','OFSA3','GSGI34','COCA34','RBRR11',
        'BOEI34','TMOS34','PQDP11','SGPS3','ENMA3B','LIPR3',
        'LILY34','LMTB34','VVAR3','TRIS3','SCHW34','ORCL34',
        'HTMX11','BRAX11','FJTA4','LUPA3','FOFT11','FDXB34',
        'TECN3','FVBI11','MILS3','RBRD11','TRPL3','BMYB34',
        'GPCP3','FLMA11','UNIP5','TESA3','BBSD11','PINE4',
        'RCSL4','BRIV3','GPIV33','ALZR11','QCOM34','AXPB34',
        'MRCK34','CREM3','AMGN34','AETB34','KLBN3','BPAN4',
        'CTNM4','FIIP11B','ARMT34','SSBR3','GDBR34','RBRF11',
        'METB34','GEPA4','CPTS11B','COTY34','TRPN3','IDVL4',
        'SDIL11','RNEW11','ACNB34','RBBV11','DUKB34','MMMC34',
        'HONB34','FIND11','EDGA11','BSAN33','TIET3','PNVL3',
        'RAPT3','SLBG34','TIFF34','BIOM3','UPSS34','BIIB34',
        'KHCB34','JBDU4','CBOP11','NSLU11','SBUB34','SPTW11',
        'AIGB34','DHER34','BONY34','XTED11','MGFF11','BBRC11',
        'ABTT34','RPMG3','REDE3','FCFL11','BAHI3','FDMO34',
        'CLGN34','ABBV34','RNDP11','MATB11','ISUS11','RPAD6',
        'BMEB4','CXRI11','TGTB34','RNEW4','BRSR3','ETER3',
        'WHRL4','HCRI11','CAMB4','EMAE4','HSHY34','CLSC4',
        'MBRF11','BLAK34','POMO3','RDNI3','ANDV34','BBYY34',
        'MOAR3','CTSH34','SSFO34','GILD34','CXTL11','BGIP3',
        'TSLA34','BPHA3','RANI3','THRA11','COLG34','ENGI3',
        'WSON33','PNVL4','UCAS3','SNSY5','BPFF11','PATI3',
        'RPAD5','JRDM11','PORD11','VLOE34','DEAI34','BRKM3',
        'SCAR3','COPH34','XBOV11','USBC34','IDNT3','TCNO3',
        'RBGS11','COCE5','SLED4','RPAD3','SHPH11','GOVE11',
        'VLOL11','BRGE3','CARE11','MSBR34','GEPA3','NPAR11',
        'MDTC34','ROST34','PLRI11','BSEV3','ELEK4','CEPE5',
        'ESRX34','INEP3','MDLZ34','BNBR3','MTSA4','USIM3',
        'FIVN11','CNES11','SPXI11','LLIS3','CGRA3','WUNI34',
        'ECOO11','EALT4','CVSH34','CRPG6','PPLA11','BEES3',
        'CXCE11B','MACY34','CTXT11','KNRE11','GMCO34','FIXX11',
        'EEEL4','PEAB4','FESA3','BAZA3','MOSC34','EURO11',
        'GPSI34','USSX34','WPLZ11','TRXL11','ALPA3','FCXO34',
        'MMXM3','FSLR34','ENGI4','HPQB34','BBVJ11','TAEE4',
        'DOMC11','TELB4','CRIV4','TELB3','TEKA4','SOND5',
        'MTIG4','CTNM3','RDES11','CTSA3','EBAY34','VGIR11',
        'BGIP4','MERC4','BPAC5','ENMT3','TRNT11','MNPR3',
        'IGBR3','TXRX4','BDLL4','RNEW3','LUXM4','SULA3',
        'CRPG3','MAXR11','NVHO11','RBDS11','BOXP34','VOTS11',
        'FJTA3','PEAB3','CSAB3','FRIO3','OUCY11')
for a in acao:

    crawl.busca(a)
    crawl.boxes()

driver.quit()
