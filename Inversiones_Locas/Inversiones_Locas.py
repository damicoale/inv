import yfinance as yf

sSep = "|"

ticker = ""
sEncabezado = ""
NroAcciones = 0
UltimoPrecio = 0.00
PrecEmpMercado = 0.00
PrecEmpValua = 0.00
HayDiv = 0.00
PrecDiv = 0.00
RentDiv = 0.00
R_PreMercVal = 0.00

tick_rat_list = (["AAPL",10],["AXP",15],["BIOX",0.5],["GLOB",18],["GOOGL",58],["KO",5], ["MCD",24],["META",24],["MSFT",30], ["VIST",1], ["WMT",6])

#["BAC",2],["C",3]
#UltimoPrecio=yf.Ticker("BIOX").info['currentPrice']
#NroAcciones=yf.Ticker("BIOX").info['sharesOutstanding']
#EmpPrecioMercado = UltimoPrecio * NroAcciones
#EmpPrecioCalculado=yf.Ticker("BIOX").info['enterpriseValue']
#Rat_EmpMerCal=EmpPrecioMercado/EmpPrecioCalculado
#Rat_DivxAcc=yf.Ticker("KO").info['dividendYield']*100
#PER=yf.Ticker("KO").info['trailingPE']
#Rcirculante=yf.Ticker("BIOX").info['currentRatio']

sEncabezado = "Ticker" + sSep
sEncabezado = sEncabezado + "Precio_ACC" + sSep

sEncabezado = sEncabezado + "Precio_CED$" + sSep
sEncabezado = sEncabezado + "Precio_CED$_NOR" + sSep
sEncabezado = sEncabezado + "Dolar" + sSep

sEncabezado = sEncabezado + "Precio_CEDD" + sSep
sEncabezado = sEncabezado + "Precio_CEDD_NOR" + sSep


sEncabezado = sEncabezado + "NroAcciones" + sSep 
sEncabezado = sEncabezado + "EmpPrecioMercado" + sSep 
sEncabezado = sEncabezado + "EmpPrecioValuado" + sSep
sEncabezado = sEncabezado + "R. PreMer/PreVal" + sSep
sEncabezado = sEncabezado + "$ Div." + sSep
sEncabezado = sEncabezado + "% Div." + sSep


print(sEncabezado)

for i in range(len(tick_rat_list)):
    ticker=tick_rat_list[i][0]
    ratio=tick_rat_list[i][1]
    cedear = ticker + ".BA"

    if ticker == "GOOGL":
        cedeard = "GOGLD.BA"
    elif ticker == "BAC":
        cedeard = "BA.CD.BA"
    else:
        cedeard = ticker + "D.BA"

    ticker_object = yf.Ticker(ticker)
    cedear_object = yf.Ticker(cedear)
    cedeard_object = yf.Ticker(cedeard)
    #print(ticker_object.info)

    UltimoPrecio = ticker_object.info['currentPrice']
    UltimoCed = cedear_object.info['currentPrice']
    UltimoCed_N = cedear_object.info['currentPrice'] * ratio
    Dolar = UltimoCed_N / UltimoPrecio
    UltimoCedD = cedeard_object.info['currentPrice'] 
    UltimoCedD_N = cedeard_object.info['currentPrice'] * ratio
    NroAcciones  = ticker_object.info['sharesOutstanding']
    PrecEmpValua = ticker_object.info['enterpriseValue']
    HayDiv = ticker_object.info['trailingAnnualDividendYield']

    #Evaluo si paga dividendos
    if HayDiv > 0:
        PrecDiv = ticker_object.info['dividendRate']
        RentDiv = PrecDiv * 100 / UltimoPrecio
    else:
        PrecDiv = 0.00
        RentDiv = 0.00

    PrecEmpMercado = UltimoPrecio * NroAcciones
    R_PreMercVal = PrecEmpMercado / PrecEmpValua

    sCadena = ticker + sSep
    sCadena = sCadena + str(UltimoPrecio) + sSep 

    sCadena = sCadena + str(UltimoCed) + sSep 
    sCadena = sCadena + str(UltimoCed_N) + sSep 
    sCadena = sCadena + str(Dolar) + sSep 

    sCadena = sCadena + str(UltimoCedD) + sSep
    sCadena = sCadena + str(UltimoCedD_N) + sSep


    sCadena = sCadena + str(NroAcciones) + sSep 
    sCadena = sCadena + str(PrecEmpMercado) + sSep 
    sCadena = sCadena + str(PrecEmpValua) + sSep 
    sCadena = sCadena + str(R_PreMercVal) + sSep
    sCadena = sCadena + str(PrecDiv) + sSep
    sCadena = sCadena + str(RentDiv) + sSep
    print(sCadena)
