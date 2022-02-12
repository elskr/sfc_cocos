#%%

#INTRODUCTION

#%matplotlib inline

from __future__ import division
from pysolve.model import Model
from pysolve.utils import is_close,round_solution

from matplotlib import rcParams, cycler
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D

#NO BAILOUT MODEL

def create_nobailout_model():
    model = Model()

    model.set_var_default(0)
    model.var('A_b1d', desc="Central bank advances actually demanded by retail banks")
    model.var('A_b1s', desc="Central bank advances supplied to retail banks")
    model.var('A_b2d', desc="Central bank advances actually demanded by investment banks")
    model.var('A_b2s', desc="Central bank advances supplied to investment banks")
    model.var('A_Nb1d', desc="Central bank advances notionally demanded by deposit banks")
    model.var('A_Nb2d', desc="Central bank advances notionally demanded by investment banks")
    model.var('B_b2d', desc="Treasury bills demanded by investment banks")
    model.var('B_b2h', desc="Treasury bills held by investment banks")
    model.var('B_b2s', desc="Treasury bills supplied to investment banks")
    model.var('B_fd', desc="Trasury bills demanded by firms")
    model.var('B_fh', desc="Treasury bills held by firms")
    model.var('B_fs', desc="Treasury bills supplied to firms")
    model.var('B_rd', desc="Treasury bills demanded by investor households")
    model.var('B_rh', desc="Treasury bills held by investor households")
    model.var('B_rs', desc="Treasury bills supplied to investor households")
    model.var('B_s', desc="Total supply of treasury bills")
    model.var('BCO1_fd', desc="Retail bank CoCos demanded by firms")
    model.var('BCO1_fh', desc="Retail bank CoCos held by firms")
    model.var('BCO1_fs', desc="Retail bank CoCos supplied to firms")
    model.var('BCO1_rd', desc="Retail bank CoCos demanded by investor households")
    model.var('BCO1_rh', desc="Retail bank CoCos held by investor households")
    model.var('BCO1_rs', desc="Retail bank CoCos supplied to investor households")
    model.var('BCO1_s', desc="Actual total supply of retail bank CoCos")
    model.var('BCO1_sN', desc="Notional total supply of retail bank CoCos")
    model.var('BCO2_fd', desc="Investment bank CoCos demanded by firms")
    model.var('BCO2_fh', desc="Investment bank CoCos held by firms")
    model.var('BCO2_fs', desc="Investment bank CoCos supplied to firms")
    model.var('BCO2_rd', desc="Investment bank CoCos demanded by investor households")
    model.var('BCO2_rh', desc="Investment bank CoCos held by investor households")
    model.var('BCO2_rs', desc="Investment bank CoCos supplied to investor households")
    model.var('BCO2_s', desc="Actual total supply of investment bank CoCos")
    model.var('BCO2_sN', desc="Notional total supply of investment bank CoCos")
    model.var('BUR_w', desc="Debt burden of worker households")
    model.var('c_r', desc="Real consumption of investor households")
    model.var('C_r', desc="Nominal consumption of investor households")
    model.var('C_w', desc="Nominal consumption of worker households")
    model.var('c_w', desc="Real consumption of investor households")
    model.var('CARb1', desc="Capital adequacy ratio of retail banks")
    model.var('CG_b2', desc="Capital gains of investment banks")
    model.var('CG_f', desc="Capital gains of firms")
    model.var('CG_r', desc="Capital gains of investor households")
    model.var('D_rd', desc="Checking deposits demanded by investor households")
    model.var('D_rh', desc="Checking deposits held by investor households")
    model.var('D_rs', desc="Checking deposits supplied to investor households")
    model.var('D_s', desc="Total supply of checking deposits")
    model.var('D_wd', desc="Checking deposits demanded by worker households")
    model.var('D_wh', desc="Checking deposits held by worker households")
    model.var('D_ws', desc="Checking deposits supplied to worker households")
    model.var('e_b2d', desc="Firm shares demanded by investment banks")
    model.var('e_b2h', desc="Firm shares held by investment banks")
    model.var('e_b2s', desc="Firm shares supplied to investment banks")
    model.var('e_rd', desc="Firm shares demanded by investor households")
    model.var('e_rh', desc="Firm shares held by investor households")
    model.var('e_rs', desc="Firm shares supplied to investor households")
    model.var('e_s', desc="Total supply of firm shares")
    model.var('ER', desc="Employment rate")
    model.var('eta', desc="Ratio of new loans to personal income")
    model.var('F_b1', desc="Retail bank profits")
    model.var('F_b2', desc="Investment banks profits")
    model.var('F_cb', desc="Central bank profits")
    model.var('F_f', desc="Firm profits")
    model.var('FD_b2f', desc="Distributed profits by firms to investment banks")
    model.var('FD_rf', desc="Distributed profits by firms to investor households")
    model.var('FD_f', desc="Total distributed profits by firms")
    model.var('FU_b1', desc="Retained earnings of retail banks")
    model.var('FU_b2', desc="Retailed earnings of investment banks")
    model.var('FU_f', desc="Retained earnings of firms")
    model.var('G', desc="Nominal government expenditures")
    model.var('g', desc="Real government expenditures")
    model.var('GD', desc="Government debt as the sum of past deficits")
    model.var('GL_wd', desc="Gross amount of new loans demanded by worker households")
    model.var('gr_k', desc="Growth of real capital stock")
    model.var('HPM_b1d', desc="Reserve requirements of retail banks")
    model.var('HPM_b1s', desc="Reserves supplied to retail banks")
    model.var('HPM_b2d', desc="Reserve requirements of investment banks")
    model.var('HPM_b2s', desc="Reserves supplied to investment banks")
    model.var('INV', desc="Gross nominal investment of firms")
    model.var('inv', desc="Gross real investment of firms")
    model.var('IN', desc="Firm stock of inventories at current costs")
    model.var('ink', desc="Firm actual real stock of inventories")
    model.var('ine', desc="Short-term inventory target of firms")
    model.var('inT', desc="Long-term investory target of firms")
    model.var('indicKRb1', desc="Condition on retail bank CoCo activation")
    model.var('indicKRb1bis', desc="Condition on retail CoCo activation")
    model.var('indicKRb2', desc="Condition on investment CoCo activation")
    model.var('indicKRb2bis', desc="Condition on investment CoCo activation")
    model.var('K', desc="Nominal capital stock of firms")
    model.var('k', desc="Real capital stock of firms")
    model.var('klim', desc="Share of rationed credit")
    model.var('KR_b1', desc="Variable controlling retail bank CoCo activation")
    model.var('KR_b2', desc="Variable controlling investment bank CoCo activation")
    model.var('l', desc="Leverage ratio of firms")
    model.var('L_fd', desc="Loans demanded by firms")
    model.var('L_fs', desc="Loans supplied to firms")
    model.var('L_wd', desc="Loans demanded by worker households")
    model.var('L_ws', desc="Loans supplied to worker households")
    model.var('LEV_w', desc="Leverage ratio of worker households")
    model.var('N', desc="Effective employment level")
    model.var('NT', desc="Desored employment level")
    model.var('NHUC', desc="Normal historic unit cost of firms")
    model.var('NL_wd', desc="Nominal net flow of new loans demanded by worker households")
    model.var('NL_ws', desc="Nominal net flow of new loans supplied to worker households")
    model.var('nl_ws', desc="Real net flow of new loans supplied to worker households")
    model.var('nl_wse', desc="Real net flow of new loans expected by households")
    model.var('NPLW', desc="Non-performing loans")
    model.var('nplw', desc="Share of non-performing loans")
    model.var('NUC', desc="Normal unit cost of firms")
    model.var('omegaT', desc="Target real wage for workers")
    model.var('p', desc="Price level")
    model.var('pbco1', desc="Price of retail bank CoCos")
    model.var('pbco2', desc="Price of investment bank CoCos")
    model.var('pe', desc="Price of firl shares")
    model.var('PE', desc="Price earnings ratio")
    model.var('PI', desc="Inflation rate")
    model.var('pr', desc="Lavor productivity du travail")
    model.var('PSBR', desc="Nominal public deficit")
    model.var('r_BCO1', desc="Return rate of retail bank CoCos")
    model.var('r_BCO2', desc="Return rate of investment bank CoCos")
    model.var('r_cf', desc="Cash flow ratio of firms")
    model.var('r_d', desc="Interest rate on checking deposits")
    model.var('r_fTOT', desc="Interests earned by firms")
    model.var('r_K', desc="Retrn rate on firm shares")
    model.var('r_l', desc="Interest rate on loans")
    model.var('r_q', desc="Tobin's Q")
    model.var('r_td', desc="Interest rate on time deposits")
    model.var('REP_w', desc="Loan repayments by worker households")
    model.var('rr_cf', desc="Real cash flow rate of firms")
    model.var('rr_l', desc="Real interest rate on loans")
    model.var('rr_q', desc="Real Tobin's Q")
    model.var('S', desc="Nominal sales at current price")
    model.var('s', desc="Real sales at current price")
    model.var('se', desc="Expected real sales")
    model.var('share_b1', desc="Share of triggered retail bank CoCos")
    model.var('share_b2', desc="Share of triggered investment bank CoCos")
    model.var('T', desc="Total taxes")
    model.var('T_r', desc="Taxes on worker household income")
    model.var('T_w', desc="Taxes on investor household income")
    model.var('TD_rd', desc="Time deposits demanded by investor households")
    model.var('TD_rh', desc="Time deposits held by investor households")
    model.var('TD_rs', desc="Time deposits supplied by investor households")
    model.var('u', desc="Capacity utilization of firms")
    model.var('UC', desc="Unit cost of firms")
    model.var('V_b1', desc="Nominal net wealth of retail banks")
    model.var('V_b2', desc="Nominal net wealth of investment banks")
    model.var('V_f', desc="Nominal net wealth of firms")
    model.var('V_r', desc="Nominal net wealth of invesor households")
    model.var('v_r', desc="Real net wealth of investor households")
    model.var('V_w', desc="Nominal net wealth of worker households")
    model.var('v_w', desc="Real net wealth of worker households")
    model.var('Vfma_b2', desc="Nominal financial net wealth of investment banks")
    model.var('Vfma_w', desc="Nominal financial net wealth of worker households")
    model.var('W', desc="Nominal wage rate")
    model.var('WB', desc="Nominal wage bill")
    model.var('y', desc="Real production of firms")
    model.var('Y', desc="Nominal GDP")
    model.var('YD_r', desc="Nominal disposable income of investor households")
    model.var('yd_r', desc="Real disposable income of investor households")
    model.var('yd_re', desc="Expected real disposable income of investor households")
    model.var('YD_w', desc="Nominal disposable income of worker households")
    model.var('yd_w', desc="Real disposable income of worker households")
    model.var('yd_we', desc="Expected real disposable income of worker households")
    model.var('YP_r', desc="Nominal income of investor households")
    model.var('YP_w', desc="Nominal income of worker households")
    model.var('z5', desc="Condition")
    model.var('z6', desc="Condition")
    model.var('pemean', desc = "pe")
    model.var('pevar', desc = "pe")
    model.var('pestd', desc = "pe")
    model.var('pegrowth', desc = "pe")
    model.var('Ygrowth', desc = "Growth rate of production")
    model.var('Cgrowth', desc = "Growth rate of consumption")
    model.var('V_rgrowth', desc = "Growth rate of investor households' net wealth")
    model.var('V_wgrowth', desc = "Growth rate of worker households' net wealth")
    model.var('V_fgrowth', desc = "Growth rate of firms' net wealth")
    model.var('V_b1growth', desc = "Growth rate of retail banks' net wealth")
    model.var('V_b2growth', desc = "Growth rate of investment banks' net wealth")
    model.var('retail_debt', desc = "Debt of the retail bank sector")
    model.var('investment_debt', desc = "Debt of the investment bank sector")
    model.var('totalbank_debt', desc = "Debt of the banking sector as a whole")
    model.var('public_debt', desc = "Public debt")
    model.var('household_debt', desc = "Debt of the household sector")
    model.var('firm_debt', desc = "Debt of the firm sector")
    model.var('private_debt', desc = "Debt of the private sector as a whole minus banks")
    model.var('private_to_public', desc = "Ratio of private-to-public debt")
    model.var('bank_to_private', desc = "Ratio of bank-to-private debt")
    model.var('bank_to_public', desc = "Ratio of bank-to-public debt")
    
    
    model.set_param_default(0)
    model.param('alpha1', desc="Propensity to consume as a function of income")
    model.param('alpha2', desc="Propensity to consume as a function of savings")
    model.param('beta', desc="Parameter related to expectation formations on real sales")
    model.param('CARTb1', desc="Target capital adequacy ratio of retail banks")
    model.param('chi1', desc="Spread between interest rate on loans and interest rate on advances")
    model.param('chi2', desc="Spread between interest rate on checking deposits and interest rate on advances")
    model.param('chi3', desc="Spread between interest rate on time deposits and interest rate on advances")
    model.param('chi4', desc="Spread between interest rate on retail CoCos and interest rate on advances")
    model.param('chi5', desc="Spread between interest rate on investment CoCos and interest rate on advances")
    model.param('delta', desc="Depreciation rate of fixed capital")
    model.param('deltarep', desc="Ratio of personal loans repayments to stock of loans")
    model.param('epsilon', desc="Parameter related to expectation formations on real disposable income")
    model.param('epsilon1', desc="Parameter reltated to expectation formations of worker households on loans supplied to them")
    model.param('epsilon20', desc="Parameter related to investment banks' demand for firm shares")
    model.param('epsilon21', desc="Parameter related to investment banks' demand for firm shares")
    model.param('epsilon22', desc="Parameter related to investment banks' demand for firm shares")
    model.param('eta0', desc="Ratio of new loans to personal income - exogenous component")
    model.param('etaw', desc="Relation between the ratio of new loans to personal income and the interest rate on loans")
    model.param('gamma', desc="Speed of adjustment of inventories to the target level")
    model.param('gamma0', desc="Exogenous component in the growth of the real stock of capital")
    model.param('gamma1', desc="Relation between the capacity utilization rate and the growth of the real stock of capital")
    model.param('gamma2', desc="Relation between the real interest rate and the growth of the real stock of capital")
    model.param('gamma3', desc="Relation between the cash flow rate and the growth of the real stock of capital")
    model.param('gamma4', desc="Relation between Tobin's Q and the growth of the real stock of capital")
    model.param('grg', desc="Growth of government expenditures")
    model.param('grpr', desc="Growth of labor productivity")
    model.param('kappa', desc="Sensitivity of investment bank coco activations to shocks")
    model.param('klim0', desc="Exogenous component of credit rationing")
    model.param('klim1', desc="Relation between worker household leverage and credit rationing")
    model.param('klim2', desc="Relation between capital adequacy ratio and credit rationing")
    model.param('klim3', desc="Relation between worker household debt burden and credit rationing")
    model.param('klim4', desc="Relation between non-performing loans and credit rationing") 
    model.param('KRT1', desc="Trigger threshold of retail bank CoCos")
    model.param('KRT2', desc="Trigger threshold of investment banks CoCos")
    model.param('lambda20', desc="Parameter related to investor household's demand for investment bank time deposits")
    model.param('lambda21', desc="Parameter related to investor household's demand for investment bank time deposits")
    model.param('lambda22', desc="Parameter related to investor household's demand for investment bank time deposits")
    model.param('lambda23', desc="Parameter related to investor household's demand for investment bank time deposits")
    model.param('lambda24', desc="Parameter related to investor household's demand for investment bank time deposits")
    model.param('lambda25', desc="Parameter related to investor household's demand for investment bank time deposits")
    model.param('lambda26', desc="Parameter related to investor household's demand for investment bank time deposits")
    model.param('lambda30', desc="Parameter related to investor household's demand for treasury bills")
    model.param('lambda31', desc="Parameter related to investor household's demand for treasury bills")
    model.param('lambda32', desc="Parameter related to investor household's demand for treasury bills")
    model.param('lambda33', desc="Parameter related to investor household's demand for treasury bills")
    model.param('lambda34', desc="Parameter related to investor household's demand for treasury bills")
    model.param('lambda35', desc="Parameter related to investor household's demand for treasury bills")
    model.param('lambda36', desc="Parameter related to investor household's demand for treasury bills")
    model.param('lambda40', desc="Parameter related to investor household's demand for firm shares")
    model.param('lambda41', desc="Parameter related to investor household's demand for firm shares")
    model.param('lambda42', desc="Parameter related to investor household's demand for firm shares")
    model.param('lambda43', desc="Parameter related to investor household's demand for firm shares")
    model.param('lambda44', desc="Parameter related to investor household's demand for firm shares")
    model.param('lambda45', desc="Parameter related to investor household's demand for firm shares")
    model.param('lambda46', desc="Parameter related to investor household's demand for firm shares")
    model.param('lambda50', desc="Parameter related to investor household's demand for retail bank CoCos")
    model.param('lambda51', desc="Parameter related to investor household's demand for retail bank CoCos")
    model.param('lambda52', desc="Parameter related to investor household's demand for retail bank CoCos")
    model.param('lambda53', desc="Parameter related to investor household's demand for retail bank CoCos")
    model.param('lambda54', desc="Parameter related to investor household's demand for retail bank CoCos")
    model.param('lambda55', desc="Parameter related to investor household's demand for retail bank CoCos")
    model.param('lambda56', desc="Parameter related to investor household's demand for retail bank CoCos")
    model.param('lambda60', desc="Parameter related to investor household's demand for investment bank CoCos")
    model.param('lambda61', desc="Parameter related to investor household's demand for investment bank CoCos")
    model.param('lambda62', desc="Parameter related to investor household's demand for investment bank CoCos")
    model.param('lambda63', desc="Parameter related to investor household's demand for investment bank CoCos")
    model.param('lambda64', desc="Parameter related to investor household's demand for investment bank CoCos")
    model.param('lambda65', desc="Parameter related to investor household's demand for investment bank CoCos")
    model.param('lambda66', desc="Parameter related to investor household's demand for investment bank CoCos")
    model.param('N_fe', desc="Full employment level")
    model.param('nplw0', desc="Exogenous component of non-performing loans")
    model.param('nplw1', desc="Relation between worker household debt burden and non-performing loans")
    model.param('omega0', desc="Exogenous component of target wage")
    model.param('omega1', desc="Relation between labor productivity and target wage")
    model.param('omega2', desc="Relation between employment rate and target wage")
    model.param('omega3', desc="Speed of wage adjustment")
    model.param('omega4', desc="Speed of employment adjustment")
    model.param('phi', desc="Mark-up rate")
    model.param('psiD', desc="Dividends to gross profits ratio")
    model.param('psiU', desc="Retained profits to investment ratio")       
    model.param('r_a', desc="Interest rate on advances")
    model.param('r_b', desc="Interest rate on treasury bills")    
    model.param('rho1', desc="Reserve requirement parameter of retail banks")    
    model.param('rho2', desc="Reserve requirements parameter of investment banks")
    model.param('sigmaN', desc="Parameter related to the normal historic unit cost")    
    model.param('sigmaT', desc="Target invetories to sales ratio")
    model.param('sigmarb1', desc="Share of CoCos supplied by retail banks to investor households")
    model.param('sigmarb2', desc="Share of CoCos supplied by investment banks to investor households")
    model.param('tau20', desc="Parameter related to firms' demand for retail bank CoCos")    
    model.param('tau21', desc="Parameter related to firms' demand for retail bank CoCos")
    model.param('tau22', desc="Parameter related to firms' demand for retail bank CoCos")
    model.param('tau23', desc="Parameter related to firms' demand for retail bank CoCos")
    model.param('tau30', desc="Parameter related to firms' demand for investment bank CoCos")    
    model.param('tau31', desc="Parameter related to firms' demand for investment bank CoCos")
    model.param('tau32', desc="Parameter related to firms' demand for investment bank CoCos")
    model.param('tau33', desc="Parameter related to firms' demand for investment bank CoCos")
    model.param('theta', desc="Taxation rate on household income")        
    model.param('upsilon', desc="Share of shares supplied by firms to investor households")
    model.param('z1', desc="Relation between retail banks' debt and their CoCo issuances")
    model.param('z2', desc="Relation between investment banks' debt and their CoCo issuances")
    model.param('zeta', desc="Share of firm retained profits used for financial investments")    

    #Worker-households' equations
    model.add('YP_w = WB + r_d(-1) * D_wh(-1)')
    model.add('T_w = theta * YP_w')
    model.add('YD_w = YP_w - T_w - r_l(-1) * L_ws(-1)')
    model.add('V_w - V_w(-1) = YD_w - C_w')
    model.add('v_w = V_w / p')
    model.add('c_w = alpha1 * (yd_we + nl_wse) + alpha2 * v_w(-1)')
    model.add('C_w = p * c_w')
    model.add('yd_we = epsilon * yd_w + (1 - epsilon) * yd_w(-1) * (1 + grpr)')
    model.add('yd_w = YD_w / p')
    model.add('GL_wd = eta * YD_w')
    model.add('eta = eta0 - etaw * rr_l')
    model.add('nl_wse = epsilon1 * nl_ws(-1) + (1 - epsilon1) * nl_wse(-1)')
    model.add('NL_wd = GL_wd - REP_w')
    model.add('REP_w = deltarep * L_ws(-1)')
    model.add('L_wd - L_wd(-1) = NL_wd - NPLW')
    model.add('BUR_w = (REP_w + r_l(-1) * L_wd(-1)) / YP_w')
    model.add('NPLW = nplw * L_ws(-1)')
    model.add('nplw = nplw0 + nplw1 * BUR_w(-1)')
    model.add('Vfma_w = V_w + L_ws')
    model.add('D_wd = Vfma_w')
    model.add('D_ws = D_wd')
    model.add('D_wh = D_ws')

    #Investor-households' equations
    model.add('YP_r = r_d(-1) * D_rh(-1) + r_td(-1) * TD_rh(-1) + r_BCO1(-1) * BCO1_rh(-1) + r_BCO2(-1) * BCO2_rh(-1) + r_b(-1) * B_rh(-1) + FD_rf')
    model.add('T_r = theta * YP_r')
    model.add('YD_r = YP_r + CG_r - T_r')
    model.add('CG_r = (pbco1 - pbco1(-1)) * BCO1_rh(-1) + (pbco2 - pbco2(-1)) * BCO2_rh(-1) + (pe - pe(-1)) * e_rh(-1)')
    model.add('V_r = V_r(-1) + YD_r - C_r - share_b1(-1) * indicKRb1bis * pbco1(-1) * BCO1_rh(-1) - share_b2(-1) * indicKRb2bis * pbco2(-1) * BCO2_rh(-1)')
    model.add('v_r = V_r / p')
    model.add('c_r = alpha1 * yd_re + alpha2 * v_r(-1)')
    model.add('C_r = p * c_r')
    model.add('yd_r = YD_r / p')
    model.add('yd_re = epsilon * yd_r + (1 - epsilon) * yd_r(-1)')
    model.add('TD_rd = V_r(-1) * (lambda20 - lambda21 * r_d + lambda22 * r_td - lambda23 * r_b - lambda24 * r_K - lambda25 * r_BCO1 - lambda26 * r_BCO2)')
    model.add('B_rd = V_r(-1) * (lambda30 - lambda31 * r_d - lambda32 * r_td + lambda33 * r_b - lambda34 * r_K - lambda35 * r_BCO1 - lambda36 * r_BCO2)')
    model.add('D_rd = V_r - TD_rs - B_rs - pe * e_rs - pbco1 * BCO1_rs - pbco2 * BCO2_rs')
    model.add('e_rd = e_rs')
    model.add('B_rs = B_rd')
    model.add('B_rh = B_rs')
    model.add('e_rh = e_rs')
    model.add('D_rs = D_rd')
    model.add('D_rh = D_rs')

    #Firms' equations
    model.add('y = se + ine - ink(-1)')
    model.add('se = beta * s(-1) + (1 - beta) * se(-1) * (1 + grpr)')
    model.add('inT = sigmaT * se')
    model.add('ine = ink(-1) + gamma * (inT - ink(-1))')
    model.add('ink = ink(-1) + (y - s)')
    model.add('gr_k = gamma0 + gamma1 * u(-1) - gamma2 * rr_l(-1) * l(-1) + gamma3 * rr_cf(-1) + gamma4 * rr_q(-1)')
    model.add('k = k(-1) * (1 + gr_k)')
    model.add('u = y / k(-1)')
    model.add('rr_l = ((1 + r_l) / (1 + PI)) - 1')
    model.add('inv = (k - k(-1)) + delta * k(-1)')
    model.add('l = L_fs / K')
    model.add('r_cf = FU_f / K(-1)')
    model.add('rr_cf = ((1 + r_cf) / (1 + PI)) - 1')
    model.add('r_q = (L_fd + pe * e_s) / (K + IN)')
    model.add('rr_q = ((1 + r_q) / (1 + PI)) - 1')    
    model.add('s = c_w + c_r + g + inv')    
    model.add('S = s * p')    
    model.add('IN = ink * UC')    
    model.add('INV = inv * p')    
    model.add('K = k * p')    
    model.add('Y = s * p + (ink - ink(-1)) * UC')    
    model.add('omegaT = omega0 + omega1 * pr + omega2 * ER')    
    model.add('ER = N(-1) / (N_fe(-1))')    
    model.add('W - W(-1) = omega3 * (omegaT * p(-1) - W(-1))')    
    model.add('pr = pr(-1) * (1 + grpr)')    
    model.add('NT = y / pr')    
    model.add('N - N(-1) = omega4 * (NT - N(-1))')    
    model.add('WB = N * W')    
    model.add('UC = WB / y')    
    model.add('NUC = W / pr')    
    model.add('NHUC = (1 - sigmaN) * NUC + sigmaN * (1 + r_l(-1)) * NUC(-1)')    
    model.add('p = (1 + phi) * NHUC')
    model.add('PI = (p - p(-1)) / p(-1)')    
    model.add('F_f = S - WB + (IN - IN(-1)) - r_l(-1) * IN(-1) + r_fTOT + CG_f')    
    model.add('FD_f = psiD * F_f(-1)')
    model.add('FD_rf = upsilon * FD_f')    
    model.add('FD_b2f = (1 - upsilon) * FD_f')    
    model.add('FU_f = F_f - FD_f - r_l(-1) * (L_fd(-1) - IN(-1))')
    model.add('L_fd = L_fd(-1) + INV + (IN - IN(-1)) - (1 - zeta) * FU_f - (e_s - e_s(-1)) * pe')    
    model.add('e_s - e_s(-1) = (1 - psiU) * INV(-1) / pe')    
    model.add('r_K = FD_f / (e_s(-1) * pe(-1))')
    model.add('PE = pe * e_s(-1) / F_f')
    model.add('r_fTOT = r_b(-1) * B_fh(-1) + r_BCO1(-1) * BCO1_fh(-1) + r_BCO2(-1) * BCO2_fh(-1)')
    model.add('CG_f = BCO1_fh(-1) * (pbco1 - pbco1(-1)) + BCO2_fh(-1) * (pbco2 - pbco2(-1))')
    model.add('V_f = V_f(-1) + zeta * FU_f - share_b1(-1) * indicKRb1bis * pbco1(-1) * BCO1_fh(-1) - share_b2(-1) * indicKRb2bis * pbco2(-1) * BCO2_fh(-1)')
    model.add('B_fd = V_f - pbco1 * BCO1_fs - pbco2 * BCO2_fs')
    model.add('e_rs = upsilon * e_s')
    model.add('e_b2s = e_s - e_rs')
    model.add('B_fs = B_fd')
    model.add('B_fh = B_fs')

    #Government's equations
    model.add('T = T_r + T_w')
    model.add('g = G / p')
    model.add('G = G(-1) * (1 + grg)') 
    model.add('PSBR = G + r_b(-1) * B_s(-1) - (T + F_cb)')
    model.add('GD - GD(-1) = PSBR')
    model.add('B_s = B_rs + B_fs + B_b2s')

    #Central Bank's equations
    
    model.add('F_cb = r_a(-1) * (A_b1s(-1) + A_b2s(-1))')
    
    #Retail banks' equations
    model.add('D_s = D_ws + D_rs')
    model.add('L_fs = L_fd')
    model.add('L_ws = L_ws(-1) + NL_ws - REP_w')
    model.add('NL_ws = klim * NL_wd')
    model.add('nl_ws = NL_ws / p')
    model.add('klim = klim0 + klim2 * (CARb1(-1) - CARTb1) - klim4 * nplw')
    model.add('LEV_w = L_ws / V_w')
    model.add('CARb1 = (V_b1 / (L_ws + L_fs))')
    model.add('HPM_b1d = rho1 * D_s')
    model.add('HPM_b1s = HPM_b1d')
    model.add('A_Nb1d = L_ws + L_fs + HPM_b1d - D_s - V_b1')
    model.add('z5 = if_true(A_Nb1d > 0)')
    model.add('A_b1d = z5 * A_Nb1d')
    model.add('A_b1s = A_b1d')
    model.add('F_b1 = r_l(-1) * (L_fs(-1) + L_ws(-1) - NPLW) - r_d(-1) * D_s(-1) - r_a(-1) * A_b1s(-1) - r_BCO1(-1) * BCO1_s(-1)')
    model.add('r_l = r_a + chi1')
    model.add('r_d = r_a - chi2')
    model.add('V_b1 = V_b1(-1) + FU_b1 - NPLW  + share_b1(-1) * indicKRb1bis * pbco1(-1) * BCO1_s(-1)')
    model.add('FU_b1 = F_b1')
    model.add('BCO1_s = (indicKRb1 + (1-share_b1(-1)) * indicKRb1bis) * BCO1_s(-1) + z1 * indicKRb1 * (D_s(-1) - D_s(-2)) / pbco1')
    model.add('BCO1_sN - BCO1_sN(-1) = z1 * (D_s(-1) - D_s(-2)) / pbco1')
    model.add('KR_b1 = CARb1')
    model.add('r_BCO1 = r_a - chi4')
    model.add('indicKRb1 = if_true(KR_b1(-1) >= KRT1)')
    model.add('indicKRb1bis = if_true(KR_b1(-1) < KRT1)')
    model.add('share_b1 = NPLW/(L_ws + L_fs)')
    model.add('BCO1_rs = sigmarb1 * BCO1_s')
    model.add('BCO1_fs = BCO1_s - BCO1_rs')
    model.add('BCO1_rd = BCO1_rs')
    model.add('BCO1_rh = BCO1_rs')
    model.add('BCO1_fd = BCO1_fs')
    model.add('BCO1_fh = BCO1_fd')

    #Investment banks' equations
    model.add('TD_rs = TD_rd')
    model.add('TD_rh = TD_rd')
    model.add('pegrowth = (pe - pe(-1)) / pe(-1)')
    model.add('pemean = (pegrowth + pegrowth(-1) + pegrowth(-2) + pegrowth(-3) + pegrowth(-4) + pegrowth(-5)) / 5')
    model.add('pevar = ((pegrowth - pemean) * (pegrowth - pemean)) / 5')
    model.add('pestd = (pevar)**0.5')
    model.add('HPM_b2d = rho2 * TD_rs')
    model.add('HPM_b2s = HPM_b2d')
    model.add('A_Nb2d = HPM_b2d + B_b2d + pe * e_b2d - TD_rs - V_b2')
    model.add('z6 = if_true(A_Nb2d >0)')
    model.add('A_b2d = A_Nb2d * z6')
    model.add('A_b2s = A_b2d')
    model.add('F_b2 = FD_b2f + CG_b2 - r_td(-1) * TD_rs(-1) - r_BCO2(-1) * BCO2_s(-1) + r_b(-1) * B_b2s(-1) - r_a(-1) * A_b2s(-1)')
    model.add('r_td = r_a - chi3')
    model.add('V_b2 = V_b2(-1) + FU_b2 + share_b2(-1) * indicKRb2bis * pbco2(-1) * BCO2_s(-1)')
    model.add('CG_b2 = e_b2h(-1) * (pe - pe(-1))')
    model.add('FU_b2 = F_b2')
    model.add('Vfma_b2 = V_b2 - HPM_b2s')
    model.add('B_b2d = Vfma_b2 - pe * e_b2s')
    model.add('BCO2_s = (indicKRb2 + (1-share_b2(-1)) * indicKRb2bis) * BCO2_s(-1) + z2 * indicKRb2 * (TD_rs(-1) - TD_rs(-2)) / pbco2')
    model.add('BCO2_sN - BCO2_sN(-1) = z2 * (TD_rs(-1) - TD_rs(-2)) / pbco2')
    model.add('KR_b2 = pestd')
    model.add('r_BCO2 = r_a - chi5')
    model.add('indicKRb2 = if_true(KR_b2(-1) < KRT2)')
    model.add('indicKRb2bis = if_true(KR_b2(-1) >= KRT2)')
    model.add('share_b2 = kappa * pestd') 
    model.add('e_b2d = e_b2s')
    model.add('BCO2_rs = sigmarb2 * BCO2_s')
    model.add('BCO2_fs = BCO2_s - BCO2_rs')
    model.add('B_b2s = B_b2d')
    model.add('B_b2h = B_b2s')
    model.add('e_b2h = e_b2s')
    model.add('BCO2_rd = BCO2_rs')
    model.add('BCO2_rh = BCO2_rs')
    model.add('BCO2_fd = BCO2_fs')
    model.add('BCO2_fh = BCO2_fd')

    #Price equations
    model.add('pbco1 = ((V_r(-1) * (lambda50 - lambda51 * r_d - lambda52 * r_td - lambda53 * r_b - lambda54 * r_K + lambda55 * r_BCO1 - lambda56 * r_BCO2)) + (V_f(-1) * (tau20 - tau21 * r_b + tau22 * r_BCO1 - tau23 * r_BCO2))) / BCO1_sN')
    model.add('pbco2 = ((V_r(-1) * (lambda60 - lambda61 * r_d - lambda62 * r_td - lambda63 * r_b - lambda64 * r_K - lambda65 * r_BCO1 + lambda66 * r_BCO2)) + (V_f(-1) * (tau30 - tau31 * r_b - tau32 * r_BCO1 + tau33 * r_BCO2))) / BCO2_sN')
    model.add('pe = ((V_r(-1) * (lambda40 - lambda41 * r_d - lambda42 * r_td - lambda43 * r_b + lambda44 * r_K - lambda45 * r_BCO1 - lambda46 * r_BCO2)) + (Vfma_b2(-1) * (epsilon20 - epsilon21 * r_b + epsilon22 * r_K))) / e_s')
    
    #Growth rates
    model.add('Ygrowth = (Y - Y(-1)) / Y(-1)')
    model.add('Cgrowth = (C_w + C_r - C_w(-1) - C_r(-1)) / (C_w(-1) + C_r(-1))')
    model.add('V_rgrowth = (V_r - V_r(-1)) / V_r(-1)')
    model.add('V_wgrowth = (V_w - V_w(-1)) / V_w(-1)')
    model.add('V_fgrowth = (V_f - V_f(-1)) / V_f(-1)')
    model.add('V_b1growth = (V_b1 - V_b1(-1)) / V_b1(-1)')
    model.add('V_b2growth = (V_b2 - V_b2(-1)) / V_b2(-1)')
    
    #Debts
    model.add('retail_debt = D_s + A_b1s + pbco1 * BCO1_s')
    model.add('investment_debt = TD_rs + A_b2s + pbco2 * BCO2_s')
    model.add('totalbank_debt = retail_debt + investment_debt')
    model.add('public_debt = GD')
    model.add('household_debt = L_ws')
    model.add('firm_debt = L_fs')
    model.add('private_debt = firm_debt + household_debt')
    
    #Debt ratios
    model.add('private_to_public = private_debt / public_debt')
    model.add('bank_to_private = totalbank_debt / private_debt')
    model.add('bank_to_public = totalbank_debt / public_debt')
   
    return model

parameters = {'chi1': 0.01962,
             'chi2': 0.01,
             'chi3': 0.0019,
             'chi4': -0.0029,
             'chi5': -0.0029,
             'alpha1': 0.75,
             'alpha2': 0.064,
             'beta': 0.5,
             'delta': 0.0667,
             'deltarep': 0.1,
             'epsilon': 0.5,
             'epsilon1': 0.5,
             'epsilon20': 0.5,
             'epsilon21': 0.05,
             'epsilon22': 0.05,
             'eta': 0.04918,                     
             'eta0': 0.073416,                     
             'etaw': 0.4,     
             'gamma': 0.45,                     
             'gamma0': -0.06,
             'gamma1': 0.1,
             'gamma2': 0.05,
             'gamma3': 0.036,
             'gamma4': 0.003,
             'kappa': 10,
             'klim0': 1,
             'klim1': 0.3,
             'klim2': 0.3,
             'klim3': 0.4,
             'klim4': 0.2,
             'lambda20': 0.1,
             'lambda21': 0.05,
             'lambda22': 0.25,
             'lambda23': 0.05,
             'lambda24': 0.05,
             'lambda25': 0.05,
             'lambda26': 0.05,
             'lambda30': 0.1,
             'lambda31': 0.05,
             'lambda32': 0.05,
             'lambda33': 0.25,
             'lambda34': 0.05,
             'lambda35': 0.05,
             'lambda36': 0.05,
             'lambda40': 0.25,
             'lambda41': 0.05,
             'lambda42': 0.05,
             'lambda43': 0.05,
             'lambda44': 0.2,
             'lambda45': 0.025,
             'lambda46': 0.025,
             'lambda50': 0.1,
             'lambda51': 0.05,
             'lambda52': 0.05,
             'lambda53': 0.05,
             'lambda54': 0.025,
             'lambda55': 0.2,
             'lambda56': 0.025,
             'lambda60': 0.1,
             'lambda61': 0.05,
             'lambda62': 0.05,
             'lambda63': 0.05,
             'lambda64': 0.025,
             'lambda65': 0.025,
             'lambda66': 0.2,
             'nplw0': 0.1,
             'nplw1': 0.25,
             'omega0': -0.20594,
             'omega1': 1,
             'omega2': 2,
             'omega3': 0.2,
             'omega4': 0.6,
             'phi': 0.3,
             'psiD': 0.25255,
             'psiU': 0.9,
             'rho1': 0.05,
             'rho2': 0.05,
             'sigmaN': 0.1666,
             'sigmaT': 0.6,
             'sigmarb1': 0.1,
             'sigmarb2': 0.1,
             'r_b': 0.009,
             'r_a': 0.009,
             'tau20': 0.2,
             'tau21': 0.05,
             'tau22': 0.1,
             'tau23': 0.05,
             'tau30': 0.2,
             'tau31': 0.05,
             'tau32': 0.05,
             'tau33': 0.1,
             'theta': 0.22844,
             'upsilon': 1/2,
             'z1': 0.05,
             'z2': 0.05,
             'zeta': 0.9}

exogenous = [('grg', 0.03),
             ('grpr', 0.06),
             ('klim', 0.97),
             ('KRT1', -100000),
             ('KRT2', 100000),
             ('CARTb1', 0.1),
             ('BUR_w', 0.06324),
             ('c_w', 212767),
             ('c_r', 212767),
             ('CARb1', 0.09245),
             ('C_r', 1526031),
             ('ER', 1),
             ('F_b1', 4130),
             ('F_b2', 4130),
             ('F_f', 1808110),
             ('FU_b1', 419039),
             ('FU_b2', 419039),
             ('FU_f', 1515380),
             ('G', 5675560),
             ('g', 633616),
             ('GL_wd', 277590),
             ('gr_k', 0.001),
             ('INV', 1691160),
             ('inv', 235791),   
             ('KR_b1', 0.2),
             ('N_fe', 87.181),
             ('N', 'N_fe'),
             ('NT', 'N_fe'),
             ('NHUC', 5.6735),
             ('NL_wd', 683593),
             ('NPLW', 309),
             ('nplw', 0.02),
             ('NUC', 5.6106),
             ('omegaT', 112852),
             ('p', 3.591539598324356),
             ('pbco1', 5),
             ('pbco2', 3),
             ('pe', 70),
             ('PE', 5.07185),
             ('PI', 0.0026),
             ('pr', 1386),
             ('PSBR', 1894780),
             ('r_q', 0.77443),
             ('r_K', 0.03008),
             ('rr_l', 0.021838),
             ('S', 8627030),
             ('s', 1202830),
             ('se', 's'),
             ('T_w', 1702410),
             ('T_r', 1702410),
             ('T', 'T_w + T_r'),
             ('u', 0.70073),
             ('UC', 5.6106),
             ('W', 23337),
             ('WB', 2034720),
             ('Y', 8660770),
             ('y', 1207530),
             ('YD_r', 564464),
             ('YD_w', 564464),
             ('yd_r', 78700),
             ('yd_w', 78700), 
             ('yd_we', 78700),
             ('yd_re', 78700),
             ('YP_r', 731587),
             ('YP_w', 731587)]

variables = [('A_b1s', 500000),
             ('A_b1d', 500000),
             ('B_s', 10000000),
             ('BCO1_s', 511200),
             ('BCO1_sN', 511200),
             ('BCO1_rs', 255600),
             ('BCO1_rd', 'BCO1_rs'),
             ('BCO1_fs', 255600),
             ('BCO1_fd', 'BCO1_fs'),
             ('BCO2_s', 5112),
             ('BCO2_sN', 5112),
             ('BCO2_rs', 2556),
             ('BCO2_rd', 'BCO2_rs'),
             ('BCO2_fs', 2556),
             ('BCO2_fd', 'BCO2_fs'),
             ('D_s', 465569),
             ('e_s', 51120),
             ('e_rs', 25560),
             ('e_rd', 'e_rs'),
             ('e_b2s', 25560),
             ('e_b2d', 'e_b2s'),
             ('GD', 5772870),
             ('HPM_b1d', 232785),
             ('HPM_b1s', 232785),
             ('HPM_b2d', 232785),
             ('HPM_b2s', 232785),
             ('IN', 1158540),
             ('ink', 406489),
             ('ine', 440566),
             ('inT', 'ink'),
             ('K', 3274440),
             ('k', 1776890),
             ('L_wd', 209231),
             ('L_ws', 209231),
             ('L_fd', 0),
             ('L_fs', 0),
             ('TD_rs', 400000),
             ('V_b1', 20653950),
             ('V_b2', 2653950),
             ('Vfma_b2', 2653950),
             ('V_f', 2653950),
             ('V_r', 9592910),
             ('V_w', 9653950),
             ('Vfma_w', 9653950),
             ('v_w', 9653950),
             ('indicKRb1', 1),
             ('indicKRb1bis', 0),
             ('indicKRb2', 1),
             ('indicKRb2bis', 0)]

#Baseline
baseline = create_nobailout_model()
baseline.set_values(parameters)
baseline.set_values(exogenous)
baseline.set_values(variables)


for _ in range(2000):
    baseline.solve(iterations=2000, threshold=1e-6)
    
#%%
        
#SCENARIO 2Aa : depreciation of the price of company shares with CoCo activation

scenar2aa = create_nobailout_model()
scenar2aa.set_values(parameters)
scenar2aa.set_values(exogenous)
scenar2aa.set_values(variables)

for _ in range(400):
    scenar2aa.solve(iterations=2000, threshold=1e-6)

scenar2aa.set_values({'KRT2': 0.015})   
scenar2aa.set_values({'lambda40': -0.3})

for _ in range(1600):
    scenar2aa.solve(iterations=2000, threshold=1e-6)
        
#SCENARIO 2Ab : depreciation of the price of company shares with CoCo activation

scenar2ab = create_nobailout_model()
scenar2ab.set_values(parameters)
scenar2ab.set_values(exogenous)
scenar2ab.set_values(variables)

for _ in range(400):
    scenar2ab.solve(iterations=2000, threshold=1e-6)
    
scenar2ab.set_values({'KRT2': 0.015})   
scenar2ab.set_values({'lambda40': -0.1})


for _ in range(1600):
    scenar2ab.solve(iterations=2000, threshold=1e-6)

#SCENARIO 2Ac : depreciation of the price of company shares with CoCo activation

scenar2ac = create_nobailout_model()
scenar2ac.set_values(parameters)
scenar2ac.set_values(exogenous)
scenar2ac.set_values(variables)

for _ in range(400):
    scenar2ac.solve(iterations=2000, threshold=1e-6)

scenar2ac.set_values({'KRT2': 0.015})    
scenar2ac.set_values({'lambda40': 0.1})

for _ in range(1600):
    scenar2ac.solve(iterations=2000, threshold=1e-6)
    
#SCENARIO 2Ba : depreciation of the price of company shares without CoCo activation

scenar2ba = create_nobailout_model()
scenar2ba.set_values(parameters)
scenar2ba.set_values(exogenous)
scenar2ba.set_values(variables)

scenar2ba.set_values({'KRT2': 100000})

for _ in range(400):
    scenar2ba.solve(iterations=2000, threshold=1e-6)

scenar2ba.set_values({'lambda40': -0.3})


for _ in range(1600):
    scenar2ba.solve(iterations=2000, threshold=1e-6)
        
#SCENARIO 2Bb : depreciation of the price of company shares without CoCo activation

scenar2bb = create_nobailout_model()
scenar2bb.set_values(parameters)
scenar2bb.set_values(exogenous)
scenar2bb.set_values(variables)

scenar2bb.set_values({'KRT2': 100000})

for _ in range(400):
    scenar2bb.solve(iterations=2000, threshold=1e-6)

scenar2bb.set_values({'lambda40': -0.1})


for _ in range(1600):
    scenar2bb.solve(iterations=2000, threshold=1e-6)
    
#SCENARIO 2Bc : depreciation of the price of company shares without CoCo activation

scenar2bc = create_nobailout_model()
scenar2bc.set_values(parameters)
scenar2bc.set_values(exogenous)
scenar2bc.set_values(variables)

scenar2bc.set_values({'KRT2': 100000})

for _ in range(400):
    scenar2bc.solve(iterations=2000, threshold=1e-6)

scenar2bc.set_values({'lambda40': 0.1})

for _ in range(1600):
    scenar2bc.solve(iterations=2000, threshold=1e-6)
    
#%%
    
caption = '''
    Figure 15 : Standard deviation of firm equity prices following a decrease in preferences for them
    '''

data1 = list()
data2 = list()
data3 = list()
data4 = list()

for i in range(390, 440):
    base = baseline.solutions[i]
    s2aa = scenar2aa.solutions[i]
    s2ab = scenar2ab.solutions[i]
    s2ac = scenar2ac.solutions[i]
    data1.append(base['pestd'])
    data2.append(s2aa['pestd'])
    data3.append(s2ab['pestd'])
    data4.append(s2ac['pestd'])

fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='-', color='k', label='baseline')
g2, = axes.plot(data2, linestyle='--', color='k', label='-55% shock')
g3, = axes.plot(data3, linestyle='-.', color='k', label='-35% shock')
g4, = axes.plot(data4, linestyle=':', color='k', label='-15% shock')

plt.legend(handles=[g1,g2,g3,g4], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%
    
caption = '''
    Figure 16 : State of the contigent convertible trigger following a decrease in preferences for
    firm equities (1 = not activated ; 0 = activated) 
    '''

data1 = list()
data2 = list()
data3 = list()
data4 = list()

for i in range(390, 440):
    base = baseline.solutions[i]
    s2aa = scenar2aa.solutions[i]
    s2ab = scenar2ab.solutions[i]
    s2ac = scenar2ac.solutions[i]
    data1.append(base['indicKRb2'])
    data2.append(s2aa['indicKRb2'])
    data3.append(s2ab['indicKRb2'])
    data4.append(s2ac['indicKRb2'])

fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='-', color='k', label='baseline')
g2, = axes.plot(data2, linestyle='--', color='k', label='-55% shock')
g3, = axes.plot(data3, linestyle='-.', color='k', label='-35% shock')
g4, = axes.plot(data4, linestyle=':', color='k', label='-15% shock')

plt.legend(handles=[g1,g2,g3,g4], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%
    
caption = '''
    Figure 17 : Evolution of the net values of investing households, relative to the scenario 
    without any activation of coco bonds, following a decrease in preferences for firm equities 
    '''

data1 = list()
data2 = list()
data3 = list()
for i in range(390,800):
    s2aa = scenar2aa.solutions[i]
    s2ba = scenar2ba.solutions[i]
    s2ab = scenar2ab.solutions[i]
    s2bb = scenar2bb.solutions[i] 
    s2ac = scenar2ac.solutions[i]
    s2bc = scenar2bc.solutions[i]
    data1.append(s2aa['V_r'] / s2ba['V_r'])
    data2.append(s2ab['V_r'] / s2bb['V_r'])
    data3.append(s2ac['V_r'] / s2bc['V_r'])
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='--', color='k', label='-55% shock')
g2, = axes.plot(data2, linestyle='-.', color='k', label='-35% shock')
g3, = axes.plot(data3, linestyle=':', color='k', label='-15% shock')

plt.legend(handles=[g1,g2,g3], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%
    
caption = '''
    Figure 18 : Evolution of the income of investing households before capital gains, relative to the scenario 
    without any activation of coco bonds, following a decrease in preferences for firm equities 
    '''

data1 = list()
data2 = list()
data3 = list()
for i in range(390,800):
    s2aa = scenar2aa.solutions[i]
    s2ba = scenar2ba.solutions[i]
    s2ab = scenar2ab.solutions[i]
    s2bb = scenar2bb.solutions[i]
    s2ac = scenar2ac.solutions[i]
    s2bc = scenar2bc.solutions[i]
    data1.append(s2aa['YP_r'] / s2ba['YP_r'])
    data2.append(s2ab['YP_r'] / s2bb['YP_r'])
    data3.append(s2ac['YP_r'] / s2bc['YP_r'])
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='--', color='k', label='-55% shock')
g2, = axes.plot(data2, linestyle='-.', color='k', label='-35% shock')
g3, = axes.plot(data3, linestyle=':', color='k', label='-15% shock')

plt.legend(handles=[g1,g2,g3], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%

caption = '''
    Figure 19 : Evolution of the capital gains of investing households, relative to the scenario 
    without any activation of coco bonds, following a decrease in preferences for firm equities 
    '''
    
data1 = list()
data2 = list()
data3 = list()
for i in range(395,800):
    s2aa = scenar2aa.solutions[i]
    s2ba = scenar2ba.solutions[i]
    s2ab = scenar2ab.solutions[i]
    s2bb = scenar2bb.solutions[i]
    s2ac = scenar2ac.solutions[i]
    s2bc = scenar2bc.solutions[i]
    data1.append(s2aa['CG_r'] / s2ba['CG_r'])
    data2.append(s2ab['CG_r'] / s2bb['CG_r'])
    data3.append(s2ac['CG_r'] / s2bc['CG_r'])
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='--', color='k', label='-55% shock')
g2, = axes.plot(data2, linestyle='-.', color='k', label='-35% shock')
g3, = axes.plot(data3, linestyle=':', color='k', label='-15% shock')

plt.legend(handles=[g1,g2,g3], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%

caption = '''
    Figure 20 : Evolution of the consumption of investing households, relative to the scenario 
    without any activation of coco bonds, following a decrease in preferences for firm equities 
    '''
    
data1 = list()
data2 = list()
data3 = list()
for i in range(395,800):
    s2aa = scenar2aa.solutions[i]
    s2ba = scenar2ba.solutions[i]
    s2ab = scenar2ab.solutions[i]
    s2bb = scenar2bb.solutions[i]
    s2ac = scenar2ac.solutions[i]
    s2bc = scenar2bc.solutions[i]
    data1.append(s2aa['C_r'] / s2ba['C_r'])
    data2.append(s2ab['C_r'] / s2bb['C_r'])
    data3.append(s2ac['C_r'] / s2bc['C_r'])
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='--', color='k', label='-55% shock')
g2, = axes.plot(data2, linestyle='-.', color='k', label='-35% shock')
g3, = axes.plot(data3, linestyle=':', color='k', label='-15% shock')

plt.legend(handles=[g1,g2,g3], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%
    
caption = '''
    Figure 21 : Evolution of the net value of firms, relative to the scenario 
    without any activation of coco bonds, following a decrease in preferences for firm equities 
    '''

data1 = list()
data2 = list()
data3 = list()
for i in range(395,800):
    s2aa = scenar2aa.solutions[i]
    s2ba = scenar2ba.solutions[i]
    s2ab = scenar2ab.solutions[i]
    s2bb = scenar2bb.solutions[i]
    s2ac = scenar2ac.solutions[i]
    s2bc = scenar2bc.solutions[i]
    data1.append(s2aa['V_f'] / s2ba['V_f'])
    data2.append(s2ab['V_f'] / s2bb['V_f'])
    data3.append(s2ac['V_f'] / s2bc['V_f'])
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='--', color='k', label='-55% shock')
g2, = axes.plot(data2, linestyle='-.', color='k', label='-35% shock')
g3, = axes.plot(data3, linestyle=':', color='k', label='-15% shock')

plt.legend(handles=[g1,g2,g3], prop={'family': 'Times New Roman', 'size':12}, loc = 'upper right')

fig.text(0.1, -.09, caption, csfont);

#%%
    
caption = '''
    Figure 22 : Evolution of the investment of firms, relative to the scenario 
    without any activation of coco bonds, following a decrease in preferences for firm equities 
    '''

data1 = list()
data2 = list()
data3 = list()
for i in range(395,800):
    s2aa = scenar2aa.solutions[i]
    s2ba = scenar2ba.solutions[i]
    s2ab = scenar2ab.solutions[i]
    s2bb = scenar2bb.solutions[i]
    s2ac = scenar2ac.solutions[i]
    s2bc = scenar2bc.solutions[i]
    data1.append(s2aa['INV'] / s2ba['INV'])
    data2.append(s2ab['INV'] / s2bb['INV'])
    data3.append(s2ac['INV'] / s2bc['INV'])
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='--', color='k', label='-55% shock')
g2, = axes.plot(data2, linestyle='-.', color='k', label='-35% shock')
g3, = axes.plot(data3, linestyle=':', color='k', label='-15% shock')

plt.legend(handles=[g1,g2,g3], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%
    
caption = '''
    Figure 23 : Evolution of the wage bill of working households, relative to the scenario 
    without any activation of coco bonds, following a decrease in preferences for firm equities 
    '''

data1 = list()
data2 = list()
data3 = list()
for i in range(395,800):
    s2aa = scenar2aa.solutions[i]
    s2ba = scenar2ba.solutions[i]
    s2ab = scenar2ab.solutions[i]
    s2bb = scenar2bb.solutions[i]
    s2ac = scenar2ac.solutions[i]
    s2bc = scenar2bc.solutions[i]
    data1.append(s2aa['WB'] / s2ba['WB'])
    data2.append(s2ab['WB'] / s2bb['WB'])
    data3.append(s2ac['WB'] / s2bc['WB'])
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='--', color='k', label='-55% shock')
g2, = axes.plot(data2, linestyle='-.', color='k', label='-35% shock')
g3, = axes.plot(data3, linestyle=':', color='k', label='-15% shock')

plt.legend(handles=[g1,g2,g3], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%
    
caption = '''
    Figure 24 : Evolution of the consumption of working households, relative to the scenario 
    without any activation of coco bonds, following a decrease in preferences for firm equities 
    '''

data1 = list()
data2 = list()
data3 = list()
for i in range(395,800):
    s2aa = scenar2aa.solutions[i]
    s2ba = scenar2ba.solutions[i]
    s2ab = scenar2ab.solutions[i]
    s2bb = scenar2bb.solutions[i]
    s2ac = scenar2ac.solutions[i]
    s2bc = scenar2bc.solutions[i]
    data1.append(s2aa['c_w'] / s2ba['c_w'])
    data2.append(s2ab['c_w'] / s2bb['c_w'])
    data3.append(s2ac['c_w'] / s2bc['c_w'])
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='--', color='k', label='-55% shock')
g2, = axes.plot(data2, linestyle='-.', color='k', label='-35% shock')
g3, = axes.plot(data3, linestyle=':', color='k', label='-15% shock')

plt.legend(handles=[g1,g2,g3], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%
    
caption = '''
    Figure 25 : Evolution of the net value of investment banks, relative to the scenario 
    without any activation of coco bonds, following a decrease in preferences for firm equities 
    '''

data1 = list()
data2 = list()
data3 = list()
for i in range(395,800):
    s2aa = scenar2aa.solutions[i]
    s2ba = scenar2ba.solutions[i]
    s2ab = scenar2ab.solutions[i]
    s2bb = scenar2bb.solutions[i]
    s2ac = scenar2ac.solutions[i]
    s2bc = scenar2bc.solutions[i]
    data1.append(s2aa['V_b2'] / s2ba['V_b2'])
    data2.append(s2ab['V_b2'] / s2bb['V_b2'])
    data3.append(s2ac['V_b2'] / s2bc['V_b2'])
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='--', color='k', label='-55% shock')
g2, = axes.plot(data2, linestyle='-.', color='k', label='-35% shock')
g3, = axes.plot(data3, linestyle=':', color='k', label='-15% shock')

plt.legend(handles=[g1,g2,g3], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%

#INSTABILITY INDICATORS

data1 = list()
data2 = list()
data3 = list()
data4 = list()
data5 = list()
data6 = list()
data7 = list()
data8 = list()
data9 = list()
data10 = list()
data11 = list()
data12 = list()

for i in range(100, 1000):
    s2aa = scenar2ab.solutions[i]
    s2ba = scenar2bb.solutions[i]
    base = baseline.solutions[i]
    data1.append(s2aa['Ygrowth'])
    data2.append(s2ba['Ygrowth'])
    data3.append(s2aa['Cgrowth'])
    data4.append(s2ba['Cgrowth'])
    data5.append(s2aa['V_rgrowth'])
    data6.append(s2ba['V_rgrowth'])
    data7.append(s2aa['V_wgrowth'])
    data8.append(s2ba['V_wgrowth'])
    data9.append(s2aa['V_fgrowth'])
    data10.append(s2ba['V_fgrowth'])
    data11.append(s2aa['V_b2growth'])
    data12.append(s2ba['V_b2growth'])

#%%
import numpy as np

print((np.std(data1))/(np.std(data2)))
print((np.std(data3))/(np.std(data4)))
print((np.std(data5))/(np.std(data6)))
print((np.std(data7))/(np.std(data8)))
print((np.std(data9))/(np.std(data10)))
print((np.std(data11))/(np.std(data12)))

#%%

#BAILOUT MODEL

def create_bailout_model():
    model = Model()

    model.set_var_default(0)
    model.var('A_b1d', desc="Central bank advances actually demanded by retail banks")
    model.var('A_b1s', desc="Central bank advances supplied to retail banks")
    model.var('A_b2d', desc="Central bank advances actually demanded by investment banks")
    model.var('A_b2s', desc="Central bank advances supplied to investment banks")
    model.var('A_Nb1d', desc="Central bank advances notionally demanded by deposit banks")
    model.var('A_Nb2d', desc="Central bank advances notionally demanded by investment banks")
    model.var('B_b2d', desc="Treasury bills demanded by investment banks")
    model.var('B_b2h', desc="Treasury bills held by investment banks")
    model.var('B_b2s', desc="Treasury bills supplied to investment banks")
    model.var('B_fd', desc="Trasury bills demanded by firms")
    model.var('B_fh', desc="Treasury bills held by firms")
    model.var('B_fs', desc="Treasury bills supplied to firms")
    model.var('B_rd', desc="Treasury bills demanded by investor households")
    model.var('B_rh', desc="Treasury bills held by investor households")
    model.var('B_rs', desc="Treasury bills supplied to investor households")
    model.var('B_s', desc="Total supply of treasury bills")
    model.var('BCO1_fd', desc="Retail bank CoCos demanded by firms")
    model.var('BCO1_fh', desc="Retail bank CoCos held by firms")
    model.var('BCO1_fs', desc="Retail bank CoCos supplied to firms")
    model.var('BCO1_rd', desc="Retail bank CoCos demanded by investor households")
    model.var('BCO1_rh', desc="Retail bank CoCos held by investor households")
    model.var('BCO1_rs', desc="Retail bank CoCos supplied to investor households")
    model.var('BCO1_s', desc="Actual total supply of retail bank CoCos")
    model.var('BCO1_sN', desc="Notional total supply of retail bank CoCos")
    model.var('BCO2_fd', desc="Investment bank CoCos demanded by firms")
    model.var('BCO2_fh', desc="Investment bank CoCos held by firms")
    model.var('BCO2_fs', desc="Investment bank CoCos supplied to firms")
    model.var('BCO2_rd', desc="Investment bank CoCos demanded by investor households")
    model.var('BCO2_rh', desc="Investment bank CoCos held by investor households")
    model.var('BCO2_rs', desc="Investment bank CoCos supplied to investor households")
    model.var('BCO2_s', desc="Actual total supply of investment bank CoCos")
    model.var('BCO2_sN', desc="Notional total supply of investment bank CoCos")
    model.var('BO_d', desc ="Bail-out money demanded by retail banks")
    model.var('BO_s', desc="Bail-out money supplied to retail banks")
    model.var('BUR_w', desc="Debt burden of worker households")
    model.var('c_r', desc="Real consumption of investor households")
    model.var('C_r', desc="Nominal consumption of investor households")
    model.var('C_w', desc="Nominal consumption of worker households")
    model.var('c_w', desc="Real consumption of investor households")
    model.var('CARb1', desc="Capital adequacy ratio of retail banks")
    model.var('CG_b2', desc="Capital gains of investment banks")
    model.var('CG_f', desc="Capital gains of firms")
    model.var('CG_r', desc="Capital gains of investor households")
    model.var('D_rd', desc="Checking deposits demanded by investor households")
    model.var('D_rh', desc="Checking deposits held by investor households")
    model.var('D_rs', desc="Checking deposits supplied to investor households")
    model.var('D_s', desc="Total supply of checking deposits")
    model.var('D_wd', desc="Checking deposits demanded by worker households")
    model.var('D_wh', desc="Checking deposits held by worker households")
    model.var('D_ws', desc="Checking deposits supplied to worker households")
    model.var('e_b2d', desc="Firm shares demanded by investment banks")
    model.var('e_b2h', desc="Firm shares held by investment banks")
    model.var('e_b2s', desc="Firm shares supplied to investment banks")
    model.var('e_rd', desc="Firm shares demanded by investor households")
    model.var('e_rh', desc="Firm shares held by investor households")
    model.var('e_rs', desc="Firm shares supplied to investor households")
    model.var('e_s', desc="Total supply of firm shares")
    model.var('ER', desc="Employment rate")
    model.var('eta', desc="Ratio of new loans to personal income")
    model.var('F_b1', desc="Retail bank profits")
    model.var('F_b2', desc="Investment banks profits")
    model.var('F_cb', desc="Central bank profits")
    model.var('F_f', desc="Firm profits")
    model.var('FD_b2f', desc="Distributed profits by firms to investment banks")
    model.var('FD_rf', desc="Distributed profits by firms to investor households")
    model.var('FD_f', desc="Total distributed profits by firms")
    model.var('FU_b1', desc="Retained earnings of retail banks")
    model.var('FU_b2', desc="Retailed earnings of investment banks")
    model.var('FU_f', desc="Retained earnings of firms")
    model.var('G', desc="Nominal government expenditures")
    model.var('g', desc="Real government expenditures")
    model.var('GD', desc="Government debt as the sum of past deficits")
    model.var('GL_wd', desc="Gross amount of new loans demanded by worker households")
    model.var('gr_k', desc="Growth of real capital stock")
    model.var('HPM_b1d', desc="Reserve requirements of retail banks")
    model.var('HPM_b1s', desc="Reserves supplied to retail banks")
    model.var('HPM_b2d', desc="Reserve requirements of investment banks")
    model.var('HPM_b2s', desc="Reserves supplied to investment banks")
    model.var('INV', desc="Gross nominal investment of firms")
    model.var('inv', desc="Gross real investment of firms")
    model.var('IN', desc="Firm stock of inventories at current costs")
    model.var('ink', desc="Firm actual real stock of inventories")
    model.var('ine', desc="Short-term inventory target of firms")
    model.var('inT', desc="Long-term investory target of firms")
    model.var('indicBO', desc="Condition on bail out transfers")
    model.var('indicKRb1', desc="Condition on retail bank CoCo activation")
    model.var('indicKRb1bis', desc="Condition on retail CoCo activation")
    model.var('indicKRb2', desc="Condition on investment CoCo activation")
    model.var('indicKRb2bis', desc="Condition on investment CoCo activation")
    model.var('K', desc="Nominal capital stock of firms")
    model.var('k', desc="Real capital stock of firms")
    model.var('klim', desc="Share of rationed credit")
    model.var('KR_b1', desc="Variable controlling retail bank CoCo activation")
    model.var('KR_b2', desc="Variable controlling investment bank CoCo activation")
    model.var('l', desc="Leverage ratio of firms")
    model.var('L_fd', desc="Loans demanded by firms")
    model.var('L_fs', desc="Loans supplied to firms")
    model.var('L_wd', desc="Loans demanded by worker households")
    model.var('L_ws', desc="Loans supplied to worker households")
    model.var('LEV_w', desc="Leverage ratio of worker households")
    model.var('N', desc="Effective employment level")
    model.var('NT', desc="Desored employment level")
    model.var('NHUC', desc="Normal historic unit cost of firms")
    model.var('NL_wd', desc="Nominal net flow of new loans demanded by worker households")
    model.var('NL_ws', desc="Nominal net flow of new loans supplied to worker households")
    model.var('nl_ws', desc="Real net flow of new loans supplied to worker households")
    model.var('nl_wse', desc="Real net flow of new loans expected by households")
    model.var('NPLW', desc="Non-performing loans")
    model.var('nplw', desc="Share of non-performing loans")
    model.var('NUC', desc="Normal unit cost of firms")
    model.var('omegaT', desc="Target real wage for workers")
    model.var('p', desc="Price level")
    model.var('pbco1', desc="Price of retail bank CoCos")
    model.var('pbco2', desc="Price of investment bank CoCos")
    model.var('pe', desc="Price of firl shares")
    model.var('PE', desc="Price earnings ratio")
    model.var('PI', desc="Inflation rate")
    model.var('pr', desc="Lavor productivity du travail")
    model.var('PSBR', desc="Nominal public deficit")
    model.var('r_BCO1', desc="Return rate of retail bank CoCos")
    model.var('r_BCO2', desc="Return rate of investment bank CoCos")
    model.var('r_cf', desc="Cash flow ratio of firms")
    model.var('r_d', desc="Interest rate on checking deposits")
    model.var('r_fTOT', desc="Interests earned by firms")
    model.var('r_K', desc="Retrn rate on firm shares")
    model.var('r_l', desc="Interest rate on loans")
    model.var('r_q', desc="Tobin's Q")
    model.var('r_td', desc="Interest rate on time deposits")
    model.var('REP_w', desc="Loan repayments by worker households")
    model.var('rr_cf', desc="Real cash flow rate of firms")
    model.var('rr_l', desc="Real interest rate on loans")
    model.var('rr_q', desc="Real Tobin's Q")
    model.var('S', desc="Nominal sales at current price")
    model.var('s', desc="Real sales at current price")
    model.var('se', desc="Expected real sales")
    model.var('share_b1', desc="Share of triggered retail bank CoCos")
    model.var('share_b2', desc="Share of triggered investment bank CoCos")
    model.var('T', desc="Total taxes")
    model.var('T_r', desc="Taxes on worker household income")
    model.var('T_w', desc="Taxes on investor household income")
    model.var('TD_rd', desc="Time deposits demanded by investor households")
    model.var('TD_rh', desc="Time deposits held by investor households")
    model.var('TD_rs', desc="Time deposits supplied by investor households")
    model.var('u', desc="Capacity utilization of firms")
    model.var('UC', desc="Unit cost of firms")
    model.var('V_b1', desc="Nominal net wealth of retail banks")
    model.var('V_b2', desc="Nominal net wealth of investment banks")
    model.var('V_f', desc="Nominal net wealth of firms")
    model.var('V_r', desc="Nominal net wealth of invesor households")
    model.var('v_r', desc="Real net wealth of investor households")
    model.var('V_w', desc="Nominal net wealth of worker households")
    model.var('v_w', desc="Real net wealth of worker households")
    model.var('Vfma_b2', desc="Nominal financial net wealth of investment banks")
    model.var('Vfma_w', desc="Nominal financial net wealth of worker households")
    model.var('W', desc="Nominal wage rate")
    model.var('WB', desc="Nominal wage bill")
    model.var('y', desc="Real production of firms")
    model.var('Y', desc="Nominal GDP")
    model.var('YD_r', desc="Nominal disposable income of investor households")
    model.var('yd_r', desc="Real disposable income of investor households")
    model.var('yd_re', desc="Expected real disposable income of investor households")
    model.var('YD_w', desc="Nominal disposable income of worker households")
    model.var('yd_w', desc="Real disposable income of worker households")
    model.var('yd_we', desc="Expected real disposable income of worker households")
    model.var('YP_r', desc="Nominal income of investor households")
    model.var('YP_w', desc="Nominal income of worker households")
    model.var('z5', desc="Condition")
    model.var('z6', desc="Condition")
    model.var('pemean', desc = "pe")
    model.var('pevar', desc = "pe")
    model.var('pestd', desc = "pe")
    model.var('pegrowth', desc = "pe")
    model.var('Ygrowth', desc = "Growth rate of production")
    model.var('Cgrowth', desc = "Growth rate of consumption")
    model.var('V_rgrowth', desc = "Growth rate of investor households' net wealth")
    model.var('V_wgrowth', desc = "Growth rate of worker households' net wealth")
    model.var('V_fgrowth', desc = "Growth rate of firms' net wealth")
    model.var('V_b1growth', desc = "Growth rate of retail banks' net wealth")
    model.var('V_b2growth', desc = "Growth rate of investment banks' net wealth")
    model.var('retail_debt', desc = "Debt of the retail bank sector")
    model.var('investment_debt', desc = "Debt of the investment bank sector")
    model.var('totalbank_debt', desc = "Debt of the banking sector as a whole")
    model.var('public_debt', desc = "Public debt")
    model.var('household_debt', desc = "Debt of the household sector")
    model.var('firm_debt', desc = "Debt of the firm sector")
    model.var('private_debt', desc = "Debt of the private sector as a whole minus banks")
    model.var('private_to_public', desc = "Ratio of private-to-public debt")
    model.var('bank_to_private', desc = "Ratio of bank-to-private debt")
    model.var('bank_to_public', desc = "Ratio of bank-to-public debt")
    
    model.set_param_default(0)
    model.param('alpha1', desc="Propensity to consume as a function of income")
    model.param('alpha2', desc="Propensity to consume as a function of savings")
    model.param('beta', desc="Parameter related to expectation formations on real sales")
    model.param('CARTb1', desc="Target capital adequacy ratio of retail banks")
    model.param('chi1', desc="Spread between interest rate on loans and interest rate on advances")
    model.param('chi2', desc="Spread between interest rate on checking deposits and interest rate on advances")
    model.param('chi3', desc="Spread between interest rate on time deposits and interest rate on advances")
    model.param('chi4', desc="Spread between interest rate on retail CoCos and interest rate on advances")
    model.param('chi5', desc="Spread between interest rate on investment CoCos and interest rate on advances")
    model.param('delta', desc="Depreciation rate of fixed capital")
    model.param('deltarep', desc="Ratio of personal loans repayments to stock of loans")
    model.param('epsilon', desc="Parameter related to expectation formations on real disposable income")
    model.param('epsilon1', desc="Parameter reltated to expectation formations of worker households on loans supplied to them")
    model.param('epsilon20', desc="Parameter related to investment banks' demand for firm shares")
    model.param('epsilon21', desc="Parameter related to investment banks' demand for firm shares")
    model.param('epsilon22', desc="Parameter related to investment banks' demand for firm shares")
    model.param('eta0', desc="Ratio of new loans to personal income - exogenous component")
    model.param('etaw', desc="Relation between the ratio of new loans to personal income and the interest rate on loans")
    model.param('gamma', desc="Speed of adjustment of inventories to the target level")
    model.param('gamma0', desc="Exogenous component in the growth of the real stock of capital")
    model.param('gamma1', desc="Relation between the capacity utilization rate and the growth of the real stock of capital")
    model.param('gamma2', desc="Relation between the real interest rate and the growth of the real stock of capital")
    model.param('gamma3', desc="Relation between the cash flow rate and the growth of the real stock of capital")
    model.param('gamma4', desc="Relation between Tobin's Q and the growth of the real stock of capital")
    model.param('grg', desc="Growth of government expenditures")
    model.param('grpr', desc="Growth of labor productivity")
    model.param('kappa', desc="Sensitivity of investment bank coco activations to shocks")
    model.param('klim0', desc="Exogenous component of credit rationing")
    model.param('klim1', desc="Relation between worker household leverage and credit rationing")
    model.param('klim2', desc="Relation between capital adequacy ratio and credit rationing")
    model.param('klim3', desc="Relation between worker household debt burden and credit rationing")
    model.param('klim4', desc="Relation between non-performing loans and credit rationing") 
    model.param('KRT1', desc="Trigger threshold of retail bank CoCos")
    model.param('KRT1bis', desc="Trigger threshold of retail bank bailouts")
    model.param('KRT2', desc="Trigger threshold of investment banks CoCos")
    model.param('lambda20', desc="Parameter related to investor household's demand for investment bank time deposits")
    model.param('lambda21', desc="Parameter related to investor household's demand for investment bank time deposits")
    model.param('lambda22', desc="Parameter related to investor household's demand for investment bank time deposits")
    model.param('lambda23', desc="Parameter related to investor household's demand for investment bank time deposits")
    model.param('lambda24', desc="Parameter related to investor household's demand for investment bank time deposits")
    model.param('lambda25', desc="Parameter related to investor household's demand for investment bank time deposits")
    model.param('lambda26', desc="Parameter related to investor household's demand for investment bank time deposits")
    model.param('lambda30', desc="Parameter related to investor household's demand for treasury bills")
    model.param('lambda31', desc="Parameter related to investor household's demand for treasury bills")
    model.param('lambda32', desc="Parameter related to investor household's demand for treasury bills")
    model.param('lambda33', desc="Parameter related to investor household's demand for treasury bills")
    model.param('lambda34', desc="Parameter related to investor household's demand for treasury bills")
    model.param('lambda35', desc="Parameter related to investor household's demand for treasury bills")
    model.param('lambda36', desc="Parameter related to investor household's demand for treasury bills")
    model.param('lambda40', desc="Parameter related to investor household's demand for firm shares")
    model.param('lambda41', desc="Parameter related to investor household's demand for firm shares")
    model.param('lambda42', desc="Parameter related to investor household's demand for firm shares")
    model.param('lambda43', desc="Parameter related to investor household's demand for firm shares")
    model.param('lambda44', desc="Parameter related to investor household's demand for firm shares")
    model.param('lambda45', desc="Parameter related to investor household's demand for firm shares")
    model.param('lambda46', desc="Parameter related to investor household's demand for firm shares")
    model.param('lambda50', desc="Parameter related to investor household's demand for retail bank CoCos")
    model.param('lambda51', desc="Parameter related to investor household's demand for retail bank CoCos")
    model.param('lambda52', desc="Parameter related to investor household's demand for retail bank CoCos")
    model.param('lambda53', desc="Parameter related to investor household's demand for retail bank CoCos")
    model.param('lambda54', desc="Parameter related to investor household's demand for retail bank CoCos")
    model.param('lambda55', desc="Parameter related to investor household's demand for retail bank CoCos")
    model.param('lambda56', desc="Parameter related to investor household's demand for retail bank CoCos")
    model.param('lambda60', desc="Parameter related to investor household's demand for investment bank CoCos")
    model.param('lambda61', desc="Parameter related to investor household's demand for investment bank CoCos")
    model.param('lambda62', desc="Parameter related to investor household's demand for investment bank CoCos")
    model.param('lambda63', desc="Parameter related to investor household's demand for investment bank CoCos")
    model.param('lambda64', desc="Parameter related to investor household's demand for investment bank CoCos")
    model.param('lambda65', desc="Parameter related to investor household's demand for investment bank CoCos")
    model.param('lambda66', desc="Parameter related to investor household's demand for investment bank CoCos")
    model.param('N_fe', desc="Full employment level")
    model.param('nplw0', desc="Exogenous component of non-performing loans")
    model.param('nplw1', desc="Relation between worker household debt burden and non-performing loans")
    model.param('omega0', desc="Exogenous component of target wage")
    model.param('omega1', desc="Relation between labor productivity and target wage")
    model.param('omega2', desc="Relation between employment rate and target wage")
    model.param('omega3', desc="Speed of wage adjustment")
    model.param('omega4', desc="Speed of employment adjustment")
    model.param('phi', desc="Mark-up rate")
    model.param('psiD', desc="Dividends to gross profits ratio")
    model.param('psiU', desc="Retained profits to investment ratio")       
    model.param('r_a', desc="Interest rate on advances")
    model.param('r_b', desc="Interest rate on treasury bills")    
    model.param('rho1', desc="Reserve requirement parameter of retail banks")    
    model.param('rho2', desc="Reserve requirements parameter of investment banks")
    model.param('sigmaN', desc="Parameter related to the normal historic unit cost")    
    model.param('sigmaT', desc="Target invetories to sales ratio")
    model.param('sigmarb1', desc="Share of CoCos supplied by retail banks to investor households")
    model.param('sigmarb2', desc="Share of CoCos supplied by investment banks to investor households")
    model.param('tau20', desc="Parameter related to firms' demand for retail bank CoCos")    
    model.param('tau21', desc="Parameter related to firms' demand for retail bank CoCos")
    model.param('tau22', desc="Parameter related to firms' demand for retail bank CoCos")
    model.param('tau23', desc="Parameter related to firms' demand for retail bank CoCos")
    model.param('tau30', desc="Parameter related to firms' demand for investment bank CoCos")    
    model.param('tau31', desc="Parameter related to firms' demand for investment bank CoCos")
    model.param('tau32', desc="Parameter related to firms' demand for investment bank CoCos")
    model.param('tau33', desc="Parameter related to firms' demand for investment bank CoCos")
    model.param('theta0', desc="Taxation rate on household income")
    model.param('theta1', desc="Increase on taxation rate on household income in case of bailouts")           
    model.param('upsilon', desc="Share of shares supplied by firms to investor households")
    model.param('xi', desc="Parameter related to the size of bail outs")
    model.param('z1', desc="Relation between retail banks' debt and their CoCo issuances")
    model.param('z2', desc="Relation between investment banks' debt and their CoCo issuances")
    model.param('zeta', desc="Share of firm retained profits used for financial investments")    

    #Worker-households' equations
    model.add('YP_w = WB + r_d(-1) * D_wh(-1)')
    model.add('T_w = (theta0 + indicBO * theta1) * YP_w')
    model.add('YD_w = YP_w - T_w - r_l(-1) * L_ws(-1)')
    model.add('V_w - V_w(-1) = YD_w - C_w')
    model.add('v_w = V_w / p')
    model.add('c_w = alpha1 * (yd_we + nl_wse) + alpha2 * v_w(-1)')
    model.add('C_w = p * c_w')
    model.add('yd_we = epsilon * yd_w + (1 - epsilon) * yd_w(-1) * (1 + grpr)')
    model.add('yd_w = YD_w / p')
    model.add('GL_wd = eta * YD_w')
    model.add('eta = eta0 - etaw * rr_l')
    model.add('nl_wse = epsilon1 * nl_ws(-1) + (1 - epsilon1) * nl_wse(-1)')
    model.add('NL_wd = GL_wd - REP_w')
    model.add('REP_w = deltarep * L_ws(-1)')
    model.add('L_wd - L_wd(-1) = NL_wd - NPLW')
    model.add('BUR_w = (REP_w + r_l(-1) * L_wd(-1)) / YP_w')
    model.add('NPLW = nplw * L_ws(-1)')
    model.add('nplw = nplw0 + nplw1 * BUR_w(-1)')
    model.add('Vfma_w = V_w + L_ws')
    model.add('D_wd = Vfma_w')
    model.add('D_ws = D_wd')
    model.add('D_wh = D_ws')

    #Investor-households' equations
    model.add('YP_r = r_d(-1) * D_rh(-1) + r_td(-1) * TD_rh(-1) + r_BCO1(-1) * BCO1_rh(-1) + r_BCO2(-1) * BCO2_rh(-1) + r_b(-1) * B_rh(-1) + FD_rf')
    model.add('T_r = (theta0 + indicBO * theta1) * YP_r')
    model.add('YD_r = YP_r + CG_r - T_r')
    model.add('CG_r = (pbco1 - pbco1(-1)) * BCO1_rh(-1) + (pbco2 - pbco2(-1)) * BCO2_rh(-1) + (pe - pe(-1)) * e_rh(-1)')
    model.add('V_r = V_r(-1) + YD_r - C_r - share_b1(-1) * indicKRb1bis * pbco1(-1) * BCO1_rh(-1) - share_b2(-1) * indicKRb2bis * pbco2(-1) * BCO2_rh(-1)')
    model.add('v_r = V_r / p')
    model.add('c_r = alpha1 * yd_re + alpha2 * v_r(-1)')
    model.add('C_r = p * c_r')
    model.add('yd_r = YD_r / p')
    model.add('yd_re = epsilon * yd_r + (1 - epsilon) * yd_r(-1)')
    model.add('TD_rd = V_r(-1) * (lambda20 - lambda21 * r_d + lambda22 * r_td - lambda23 * r_b - lambda24 * r_K - lambda25 * r_BCO1 - lambda26 * r_BCO2)')
    model.add('B_rd = V_r(-1) * (lambda30 - lambda31 * r_d - lambda32 * r_td + lambda33 * r_b - lambda34 * r_K - lambda35 * r_BCO1 - lambda36 * r_BCO2)')
    model.add('D_rd = V_r - TD_rs - B_rs - pe * e_rs - pbco1 * BCO1_rs - pbco2 * BCO2_rs')
    model.add('e_rd = e_rs')
    model.add('B_rs = B_rd')
    model.add('B_rh = B_rs')
    model.add('e_rh = e_rs')
    model.add('D_rs = D_rd')
    model.add('D_rh = D_rs')

    #Firms' equations
    model.add('y = se + ine - ink(-1)')
    model.add('se = beta * s(-1) + (1 - beta) * se(-1) * (1 + grpr)')
    model.add('inT = sigmaT * se')
    model.add('ine = ink(-1) + gamma * (inT - ink(-1))')
    model.add('ink = ink(-1) + (y - s)')
    model.add('gr_k = gamma0 + gamma1 * u(-1) - gamma2 * rr_l(-1) * l(-1) + gamma3 * rr_cf(-1) + gamma4 * rr_q(-1)')
    model.add('k = k(-1) * (1 + gr_k)')
    model.add('u = y / k(-1)')
    model.add('rr_l = ((1 + r_l) / (1 + PI)) - 1')
    model.add('inv = (k - k(-1)) + delta * k(-1)')
    model.add('l = L_fs / K')
    model.add('r_cf = FU_f / K(-1)')
    model.add('rr_cf = ((1 + r_cf) / (1 + PI)) - 1')
    model.add('r_q = (L_fd + pe * e_s) / (K + IN)')
    model.add('rr_q = ((1 + r_q) / (1 + PI)) - 1')    
    model.add('s = c_w + c_r + g + inv')    
    model.add('S = s * p')    
    model.add('IN = ink * UC')    
    model.add('INV = inv * p')    
    model.add('K = k * p')    
    model.add('Y = s * p + (ink - ink(-1)) * UC')    
    model.add('omegaT = omega0 + omega1 * pr + omega2 * ER')    
    model.add('ER = N(-1) / (N_fe(-1))')    
    model.add('W - W(-1) = omega3 * (omegaT * p(-1) - W(-1))')    
    model.add('pr = pr(-1) * (1 + grpr)')    
    model.add('NT = y / pr')    
    model.add('N - N(-1) = omega4 * (NT - N(-1))')    
    model.add('WB = N * W')    
    model.add('UC = WB / y')    
    model.add('NUC = W / pr')    
    model.add('NHUC = (1 - sigmaN) * NUC + sigmaN * (1 + r_l(-1)) * NUC(-1)')    
    model.add('p = (1 + phi) * NHUC')
    model.add('PI = (p - p(-1)) / p(-1)')    
    model.add('F_f = S - WB + (IN - IN(-1)) - r_l(-1) * IN(-1) + r_fTOT + CG_f')    
    model.add('FD_f = psiD * F_f(-1)')
    model.add('FD_rf = upsilon * FD_f')    
    model.add('FD_b2f = (1 - upsilon) * FD_f')    
    model.add('FU_f = F_f - FD_f - r_l(-1) * (L_fd(-1) - IN(-1))')
    model.add('L_fd = L_fd(-1) + INV + (IN - IN(-1)) - (1 - zeta) * FU_f - (e_s - e_s(-1)) * pe')    
    model.add('e_s - e_s(-1) = (1 - psiU) * INV(-1) / pe')    
    model.add('r_K = FD_f / (e_s(-1) * pe(-1))')
    model.add('PE = pe * e_s(-1) / F_f')
    model.add('r_fTOT = r_b(-1) * B_fh(-1) + r_BCO1(-1) * BCO1_fh(-1) + r_BCO2(-1) * BCO2_fh(-1)')
    model.add('CG_f = BCO1_fh(-1) * (pbco1 - pbco1(-1)) + BCO2_fh(-1) * (pbco2 - pbco2(-1))')
    model.add('V_f = V_f(-1) + zeta * FU_f - share_b1(-1) * indicKRb1bis * pbco1(-1) * BCO1_fh(-1) - share_b2(-1) * indicKRb2bis * pbco2(-1) * BCO2_fh(-1)')
    model.add('B_fd = V_f - pbco1 * BCO1_fs - pbco2 * BCO2_fs')
    model.add('e_rs = upsilon * e_s')
    model.add('e_b2s = e_s - e_rs')
    model.add('B_fs = B_fd')
    model.add('B_fh = B_fs')

    #Government's equations
    model.add('T = T_r + T_w')
    model.add('g = G / p')
    model.add('G = G(-1) * (1 + grg)') 
    model.add('PSBR = G + r_b(-1) * B_s(-1) - (T + F_cb) + indicBO * BO_s')
    model.add('GD - GD(-1) = PSBR')
    model.add('B_s = B_rs + B_fs + B_b2s')
    model.add('BO_s = BO_d')
    model.add('indicBO = if_true(KR_b1(-3) < KRT1bis)')

    #Central Bank's equations
    
    model.add('F_cb = r_a(-1) * (A_b1s(-1) + A_b2s(-1))')
    
    #Retail banks' equations
    model.add('D_s = D_ws + D_rs')
    model.add('L_fs = L_fd')
    model.add('L_ws = L_ws(-1) + NL_ws - REP_w')
    model.add('NL_ws = klim * NL_wd')
    model.add('nl_ws = NL_ws / p')
    model.add('klim = klim0 + klim2 * (CARb1(-1) - CARTb1) - klim4 * nplw')
    model.add('LEV_w = L_ws / V_w')
    model.add('CARb1 = (V_b1 / (L_ws + L_fs))')
    model.add('HPM_b1d = rho1 * D_s')
    model.add('HPM_b1s = HPM_b1d')
    model.add('A_Nb1d = L_ws + L_fs + HPM_b1d - D_s - V_b1')
    model.add('z5 = if_true(A_Nb1d > 0)')
    model.add('A_b1d = z5 * A_Nb1d')
    model.add('A_b1s = A_b1d')
    model.add('F_b1 = r_l(-1) * (L_fs(-1) + L_ws(-1) - NPLW) - r_d(-1) * D_s(-1) - r_a(-1) * A_b1s(-1) - r_BCO1(-1) * BCO1_s(-1) + indicBO * BO_s')
    model.add('r_l = r_a + chi1')
    model.add('r_d = r_a - chi2')
    model.add('V_b1 = V_b1(-1) + FU_b1 - NPLW  + share_b1(-1) * indicKRb1bis * pbco1(-1) * BCO1_s(-1)')
    model.add('FU_b1 = F_b1')
    model.add('BCO1_s = (indicKRb1 + (1-share_b1(-1)) * indicKRb1bis) * BCO1_s(-1) + z1 * indicKRb1 * (D_s(-1) - D_s(-2)) / pbco1')
    model.add('BCO1_sN - BCO1_sN(-1) = z1 * (D_s(-1) - D_s(-2)) / pbco1')
    model.add('KR_b1 = CARb1')
    model.add('r_BCO1 = r_a + chi4')
    model.add('indicKRb1 = if_true(KR_b1(-1) >= KRT1)')
    model.add('indicKRb1bis = if_true(KR_b1(-1) < KRT1)')
    model.add('share_b1 = NPLW/(L_ws + L_fs)')
    model.add('BCO1_rs = sigmarb1 * BCO1_s')
    model.add('BCO1_fs = BCO1_s - BCO1_rs')
    model.add('BCO1_rd = BCO1_rs')
    model.add('BCO1_rh = BCO1_rs')
    model.add('BCO1_fd = BCO1_fs')
    model.add('BCO1_fh = BCO1_fd')
    model.add('BO_d = indicBO * NPLW')

    #Investment banks' equations
    model.add('TD_rs = TD_rd')
    model.add('TD_rh = TD_rd')
    model.add('pegrowth = (pe - pe(-1)) / pe(-1)')
    model.add('pemean = (pegrowth + pegrowth(-1) + pegrowth(-2) + pegrowth(-3) + pegrowth(-4) + pegrowth(-5)) / 5')
    model.add('pevar = ((pegrowth - pemean) * (pegrowth - pemean)) / 5')
    model.add('pestd = (pevar)**0.5')
    model.add('HPM_b2d = rho2 * TD_rs')
    model.add('HPM_b2s = HPM_b2d')
    model.add('A_Nb2d = HPM_b2d + B_b2d + pe * e_b2d - TD_rs - V_b2')
    model.add('z6 = if_true(A_Nb2d >0)')
    model.add('A_b2d = A_Nb2d * z6')
    model.add('A_b2s = A_b2d')
    model.add('F_b2 = FD_b2f + CG_b2 - r_td(-1) * TD_rs(-1) - r_BCO2(-1) * BCO2_s(-1) + r_b(-1) * B_b2s(-1) - r_a(-1) * A_b2s(-1)')
    model.add('r_td = r_a - chi3')
    model.add('V_b2 = V_b2(-1) + FU_b2 + share_b2(-1) * indicKRb2bis * pbco2(-1) * BCO2_s(-1)')
    model.add('CG_b2 = e_b2h(-1) * (pe - pe(-1))')
    model.add('FU_b2 = F_b2')
    model.add('Vfma_b2 = V_b2 - HPM_b2s')
    model.add('B_b2d = Vfma_b2 - pe * e_b2s')
    model.add('BCO2_s = (indicKRb2 + (1-share_b2(-1)) * indicKRb2bis) * BCO2_s(-1) + z2 * indicKRb2 * (TD_rs(-1) - TD_rs(-2)) / pbco2')
    model.add('BCO2_sN - BCO2_sN(-1) = z2 * (TD_rs(-1) - TD_rs(-2)) / pbco2')
    model.add('KR_b2 = pestd')
    model.add('r_BCO2 = r_a + chi5')
    model.add('indicKRb2 = if_true(KR_b2(-1) < KRT2)')
    model.add('indicKRb2bis = if_true(KR_b2(-1) >= KRT2)')
    model.add('share_b2 = kappa * pestd') 
    model.add('e_b2d = e_b2s')
    model.add('BCO2_rs = sigmarb2 * BCO2_s')
    model.add('BCO2_fs = BCO2_s - BCO2_rs')
    model.add('B_b2s = B_b2d')
    model.add('B_b2h = B_b2s')
    model.add('e_b2h = e_b2s')
    model.add('BCO2_rd = BCO2_rs')
    model.add('BCO2_rh = BCO2_rs')
    model.add('BCO2_fd = BCO2_fs')
    model.add('BCO2_fh = BCO2_fd')

    #Price equations
    model.add('pbco1 = ((V_r(-1) * (lambda50 - lambda51 * r_d - lambda52 * r_td - lambda53 * r_b - lambda54 * r_K + lambda55 * r_BCO1 - lambda56 * r_BCO2)) + (V_f(-1) * (tau20 - tau21 * r_b + tau22 * r_BCO1 - tau23 * r_BCO2))) / BCO1_sN')
    model.add('pbco2 = ((V_r(-1) * (lambda60 - lambda61 * r_d - lambda62 * r_td - lambda63 * r_b - lambda64 * r_K - lambda65 * r_BCO1 + lambda66 * r_BCO2)) + (V_f(-1) * (tau30 - tau31 * r_b - tau32 * r_BCO1 + tau33 * r_BCO2))) / BCO2_sN')
    model.add('pe = ((V_r(-1) * (lambda40 - lambda41 * r_d - lambda42 * r_td - lambda43 * r_b + lambda44 * r_K - lambda45 * r_BCO1 - lambda46 * r_BCO2)) + (Vfma_b2(-1) * (epsilon20 - epsilon21 * r_b + epsilon22 * r_K))) / e_s')
    
    #Growth rates
    model.add('Ygrowth = (Y - Y(-1)) / Y(-1)')
    model.add('Cgrowth = (C_w + C_r - C_w(-1) - C_r(-1)) / (C_w(-1) + C_r(-1))')
    model.add('V_rgrowth = (V_r - V_r(-1)) / V_r(-1)')
    model.add('V_wgrowth = (V_w - V_w(-1)) / V_w(-1)')
    model.add('V_fgrowth = (V_f - V_f(-1)) / V_f(-1)')
    model.add('V_b1growth = (V_b1 - V_b1(-1)) / V_b1(-1)')
    model.add('V_b2growth = (V_b2 - V_b2(-1)) / V_b2(-1)')
    
    #Debts
    model.add('retail_debt = D_s + A_b1s + pbco1 * BCO1_s')
    model.add('investment_debt = TD_rs + A_b2s + pbco2 * BCO2_s')
    model.add('totalbank_debt = retail_debt + investment_debt')
    model.add('public_debt = GD')
    model.add('household_debt = L_ws')
    model.add('firm_debt = L_fs')
    model.add('private_debt = firm_debt + household_debt')
    
    #Debt ratios
    model.add('private_to_public = private_debt / public_debt')
    model.add('bank_to_private = totalbank_debt / private_debt')
    model.add('bank_to_public = totalbank_debt / public_debt')
        
    return model

parameters = {'chi1': 0.01962,
             'chi2': 0.01,
             'chi3': 0.0019,
             'chi4': 0.0029,
             'chi5': 0.0029,
             'alpha1': 0.75,
             'alpha2': 0.064,
             'beta': 0.5,
             'delta': 0.0667,
             'deltarep': 0.1,
             'epsilon': 0.5,
             'epsilon1': 0.5,
             'epsilon20': 0.5,
             'epsilon21': 0.05,
             'epsilon22': 0.05,
             'eta': 0.04918,                     
             'eta0': 0.073416,                     
             'etaw': 0.4,     
             'gamma': 0.45,                     
             'gamma0': -0.06,
             'gamma1': 0.1,
             'gamma2': 0.05,
             'gamma3': 0.036,
             'gamma4': 0.003,
             'kappa': 10,
             'klim0': 1,
             'klim1': 0.3,
             'klim2': 0.3,
             'klim3': 0.4,
             'klim4': 0.2,
             'lambda20': 0.1,
             'lambda21': 0.05,
             'lambda22': 0.25,
             'lambda23': 0.05,
             'lambda24': 0.05,
             'lambda25': 0.05,
             'lambda26': 0.05,
             'lambda30': 0.1,
             'lambda31': 0.05,
             'lambda32': 0.05,
             'lambda33': 0.25,
             'lambda34': 0.05,
             'lambda35': 0.05,
             'lambda36': 0.05,
             'lambda40': 0.25,
             'lambda41': 0.05,
             'lambda42': 0.05,
             'lambda43': 0.05,
             'lambda44': 0.2,
             'lambda45': 0.025,
             'lambda46': 0.025,
             'lambda50': 0.1,
             'lambda51': 0.05,
             'lambda52': 0.05,
             'lambda53': 0.05,
             'lambda54': 0.025,
             'lambda55': 0.2,
             'lambda56': 0.025,
             'lambda60': 0.1,
             'lambda61': 0.05,
             'lambda62': 0.05,
             'lambda63': 0.05,
             'lambda64': 0.025,
             'lambda65': 0.025,
             'lambda66': 0.2,
             'nplw0': 0.1,
             'nplw1': 0.25,
             'omega0': -0.20594,
             'omega1': 1,
             'omega2': 2,
             'omega3': 0.2,
             'omega4': 0.6,
             'phi': 0.3,
             'psiD': 0.25255,
             'psiU': 0.9,
             'rho1': 0.05,
             'rho2': 0.05,
             'sigmaN': 0.1666,
             'sigmaT': 0.6,
             'sigmarb1': 0.1,
             'sigmarb2': 0.1,
             'r_b': 0.009,
             'r_a': 0.009,
             'tau20': 0.2,
             'tau21': 0.05,
             'tau22': 0.1,
             'tau23': 0.05,
             'tau30': 0.2,
             'tau31': 0.05,
             'tau32': 0.05,
             'tau33': 0.1,
             'theta0': 0.22844,
             'theta1': 0.05,
             'upsilon': 1/2,
             'xi': 0.40,
             'z1': 0.05,
             'z2': 0.05,
             'zeta': 0.9}

exogenous = [('grg', 0.03),
             ('grpr', 0.06),
             ('klim', 0.97),
             ('KRT1', -100000),
             ('KRT1bis', -100000),
             ('KRT2', 100000),
             ('CARTb1', 0.1),
             ('BUR_w', 0.06324),
             ('c_w', 212767),
             ('c_r', 212767),
             ('CARb1', 0.09245),
             ('C_r', 1526031),
             ('ER', 1),
             ('F_b1', 4130),
             ('F_b2', 4130),
             ('F_f', 1808110),
             ('FU_b1', 419039),
             ('FU_b2', 419039),
             ('FU_f', 1515380),
             ('G', 5675560),
             ('g', 633616),
             ('GL_wd', 277590),
             ('gr_k', 0.001),
             ('INV', 1691160),
             ('inv', 235791),   
             ('KR_b1', 0.2),
             ('N_fe', 87.181),
             ('N', 'N_fe'),
             ('NT', 'N_fe'),
             ('NHUC', 5.6735),
             ('NL_wd', 683593),
             ('NPLW', 309),
             ('nplw', 0.02),
             ('NUC', 5.6106),
             ('omegaT', 112852),
             ('p', 3.591539598324356),
             ('pbco1', 5),
             ('pbco2', 3),
             ('pe', 70),
             ('PE', 5.07185),
             ('PI', 0.0026),
             ('pr', 1386),
             ('PSBR', 1894780),
             ('r_q', 0.77443),
             ('r_K', 0.03008),
             ('rr_l', 0.021838),
             ('S', 8627030),
             ('s', 1202830),
             ('se', 's'),
             ('T_w', 1702410),
             ('T_r', 1702410),
             ('T', 'T_w + T_r'),
             ('u', 0.70073),
             ('UC', 5.6106),
             ('W', 23337),
             ('WB', 2034720),
             ('Y', 8660770),
             ('y', 1207530),
             ('YD_r', 564464),
             ('YD_w', 564464),
             ('yd_r', 78700),
             ('yd_w', 78700), 
             ('yd_we', 78700),
             ('yd_re', 78700),
             ('YP_r', 731587),
             ('YP_w', 731587)]

variables = [('A_b1s', 500000),
             ('A_b1d', 500000),
             ('B_s', 10000000),
             ('BCO1_s', 511200),
             ('BCO1_sN', 511200),
             ('BCO1_rs', 255600),
             ('BCO1_rd', 'BCO1_rs'),
             ('BCO1_fs', 255600),
             ('BCO1_fd', 'BCO1_fs'),
             ('BCO2_s', 5112),
             ('BCO2_sN', 5112),
             ('BCO2_rs', 2556),
             ('BCO2_rd', 'BCO2_rs'),
             ('BCO2_fs', 2556),
             ('BCO2_fd', 'BCO2_fs'),
             ('D_s', 465569),
             ('e_s', 51120),
             ('e_rs', 25560),
             ('e_rd', 'e_rs'),
             ('e_b2s', 25560),
             ('e_b2d', 'e_b2s'),
             ('GD', 5772870),
             ('HPM_b1d', 232785),
             ('HPM_b1s', 232785),
             ('HPM_b2d', 232785),
             ('HPM_b2s', 232785),
             ('IN', 1158540),
             ('ink', 406489),
             ('ine', 440566),
             ('inT', 'ink'),
             ('K', 3274440),
             ('k', 1776890),
             ('L_wd', 209231),
             ('L_ws', 209231),
             ('L_fd', 0),
             ('L_fs', 0),
             ('TD_rs', 400000),
             ('V_b1', 20653950),
             ('V_b2', 2653950),
             ('Vfma_b2', 2653950),
             ('V_f', 2653950),
             ('V_r', 9592910),
             ('V_w', 9653950),
             ('Vfma_w', 9653950),
             ('v_w', 9653950),
             ('indicKRb1', 1),
             ('indicKRb1bis', 0),
             ('indicKRb2', 1),
             ('indicKRb2bis', 0)]

#Baseline
baseline2 = create_bailout_model()
baseline2.set_values(parameters)
baseline2.set_values(exogenous)
baseline2.set_values(variables)

for _ in range(2000):
    baseline2.solve(iterations=2000, threshold=1e-6)
    
#%%
        
#SCENARIO 3Aa : increase in defaulted loans (+5%) with CoCo activation and bailouts

scenar3aa = create_bailout_model()
scenar3aa.set_values(parameters)
scenar3aa.set_values(exogenous)
scenar3aa.set_values(variables)

for _ in range(440):
    scenar3aa.solve(iterations=2000, threshold=1e-6)

scenar3aa.set_values({'KRT1': 0.74})
scenar3aa.set_values({'KRT1bis': 0.68})    
scenar3aa.set_values({'nplw0': 0.15})

for _ in range(10):
    scenar3aa.solve(iterations=2000, threshold=1e-6)
    
scenar3aa.set_values({'nplw0': 0.1})

for _ in range(1550):
    scenar3aa.solve(iterations=2000, threshold=1e-6)
       
#SCENARIO 3Ab : increase in defaulted loans (+15%) with CoCo activation and bailouts

scenar3ab = create_bailout_model()
scenar3ab.set_values(parameters)
scenar3ab.set_values(exogenous)
scenar3ab.set_values(variables)

for _ in range(440):

    scenar3ab.solve(iterations=2000, threshold=1e-6)

scenar3ab.set_values({'KRT1': 0.74})
scenar3ab.set_values({'KRT1bis': 0.68})
scenar3ab.set_values({'nplw0': 0.25})

for _ in range(10):
    scenar3ab.solve(iterations=2000, threshold=1e-6)
    
scenar3ab.set_values({'nplw0': 0.1})

for _ in range(1550):
    scenar3ab.solve(iterations=2000, threshold=1e-6)
        
#SCENARIO 3Ac : increase in defaulted loans (+25%) with CoCo activation and bailouts

scenar3ac = create_bailout_model()
scenar3ac.set_values(parameters)
scenar3ac.set_values(exogenous)
scenar3ac.set_values(variables)

for _ in range(440):
    scenar3ac.solve(iterations=2000, threshold=1e-6)
    
scenar3ac.set_values({'KRT1': 0.74})
scenar3ac.set_values({'KRT1bis': 0.68})
scenar3ac.set_values({'nplw0': 0.35})

for _ in range(10):
    scenar3ac.solve(iterations=2000, threshold=1e-6)
    
scenar3ac.set_values({'nplw0': 0.1})

for _ in range(1550):
    scenar3ac.solve(iterations=2000, threshold=1e-6)
       
#SCENARIO 3Ad : increase in defaulted loans (+35%) with CoCo activation and bailouts

scenar3ad = create_bailout_model()
scenar3ad.set_values(parameters)
scenar3ad.set_values(exogenous)
scenar3ad.set_values(variables)

for _ in range(440):
    scenar3ad.solve(iterations=2000, threshold=1e-6)
    
scenar3ad.set_values({'KRT1': 0.74})
scenar3ad.set_values({'KRT1bis': 0.68})
scenar3ad.set_values({'nplw0': 0.45})

for _ in range(10):
    scenar3ad.solve(iterations=2000, threshold=1e-6)
    
scenar3ad.set_values({'nplw0': 0.1})

for _ in range(1550):
    scenar3ad.solve(iterations=2000, threshold=1e-6)
     
#SCENARIO 3Ba : increase in defaulted loans (+5%) without CoCo activation but with bailouts

scenar3ba = create_bailout_model()
scenar3ba.set_values(parameters)
scenar3ba.set_values(exogenous)
scenar3ba.set_values(variables)

scenar3ba.set_values({'KRT1': -100000})

for _ in range(440):
    scenar3ba.solve(iterations=2000, threshold=1e-6)

scenar3ba.set_values({'KRT1bis': 0.68})        
scenar3ba.set_values({'nplw0': 0.15})

for _ in range(10):
    scenar3ba.solve(iterations=2000, threshold=1e-6)
    
scenar3ba.set_values({'nplw0': 0.1})

for _ in range(1550):
    scenar3ba.solve(iterations=2000, threshold=1e-6)

#SCENARIO 3Bb : increase in defaulted loans (+15%) without CoCo activation but with bailouts

scenar3bb = create_bailout_model()
scenar3bb.set_values(parameters)
scenar3bb.set_values(exogenous)
scenar3bb.set_values(variables)

scenar3bb.set_values({'KRT1': -100000})

for _ in range(440):
    scenar3bb.solve(iterations=2000, threshold=1e-6)

scenar3bb.set_values({'KRT1bis': 0.68})       
scenar3bb.set_values({'nplw0': 0.25})

for _ in range(10):
    scenar3bb.solve(iterations=2000, threshold=1e-6)
    
scenar3bb.set_values({'nplw0': 0.1})

for _ in range(1550):
    scenar3bb.solve(iterations=2000, threshold=1e-6)

#SCENARIO 3Bc : increase in defaulted loans (+25%) without CoCo activation but with bailouts

scenar3bc = create_bailout_model()
scenar3bc.set_values(parameters)
scenar3bc.set_values(exogenous)
scenar3bc.set_values(variables)

scenar3bc.set_values({'KRT1': -100000})

for _ in range(440):
    scenar3bc.solve(iterations=2000, threshold=1e-6)

scenar3bc.set_values({'KRT1bis': 0.68})       
scenar3bc.set_values({'nplw0': 0.35})


for _ in range(10):
    scenar3bc.solve(iterations=2000, threshold=1e-6)
    
scenar3bc.set_values({'nplw0': 0.1})

for _ in range(1550):
    scenar3bc.solve(iterations=2000, threshold=1e-6)

#SCENARIO 3Bd : increase in defaulted loans (+35%) without CoCo activation but with bailouts

scenar3bd = create_bailout_model()
scenar3bd.set_values(parameters)
scenar3bd.set_values(exogenous)
scenar3bd.set_values(variables)

for _ in range(440):
    scenar3bd.solve(iterations=2000, threshold=1e-6)
    
scenar3bd.set_values({'KRT1bis': 0.68})
scenar3bd.set_values({'nplw0': 0.45})

for _ in range(10):
    scenar3bd.solve(iterations=2000, threshold=1e-6)
    
scenar3bd.set_values({'nplw0': 0.1})

for _ in range(1550):
    scenar3bd.solve(iterations=2000, threshold=1e-6)

#%%
    
caption = '''
    Figure 1 : Evolution of the capital adequacy ratio of banks, relative to 
    the scenario without any activation of coco bonds, following an increase in the share
    of defaulted loans'''

data1 = list()
data2 = list()
data3 = list()
data4 = list()
data5 = list()
for i in range(400, 600):
    s3aa = scenar3aa.solutions[i]
    s3ba = scenar3ba.solutions[i]
    s3ab = scenar3ab.solutions[i]
    s3bb = scenar3bb.solutions[i]
    s3ac = scenar3ac.solutions[i]
    s3bc = scenar3bc.solutions[i]
    s3ad = scenar3ad.solutions[i]
    s3bd = scenar3bd.solutions[i]
    base = baseline2.solutions[i]
    data1.append((base['CARb1']))
    data2.append((s3aa['CARb1']))
    data3.append((s3ab['CARb1']))
    data4.append((s3ac['CARb1']))
    data5.append((s3ad['CARb1']))
       
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='-', color='k', label='Baseline')
g2, = axes.plot(data2, linestyle='--', color='k', label='+5% shock')
g3, = axes.plot(data3, linestyle='-.', color='k', label='+15% shock')
g4, = axes.plot(data4, linestyle=':', color='k', label='+25% shock')
g5, = axes.plot(data5, dashes=[10, 5, 20, 5], color='k', label='+35% shock')

plt.legend(handles=[g1,g2,g3,g4,g5], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.12, caption, csfont);


#%%

caption = '''
    Figure 2 : State of the contigent convertible trigger following an increase in defaulted loans 
    (1 = not activated ; 0 = activated) '''
    
data1 = list()
data2 = list()
data3 = list()
data4 = list()
data5 = list()

for i in range(440, 480):
    s3aa = scenar3aa.solutions[i]
    s3ba = scenar3ba.solutions[i]
    s3ab = scenar3ab.solutions[i]
    s3bb = scenar3bb.solutions[i]
    s3ac = scenar3ac.solutions[i]
    s3bc = scenar3bc.solutions[i]
    s3ad = scenar3ad.solutions[i]
    s3bd = scenar3bd.solutions[i]
    base = baseline2.solutions[i]
    data1.append((base['indicKRb1']))    
    data2.append((s3aa['indicKRb1']))
    data3.append((s3ab['indicKRb1']))
    data4.append((s3ac['indicKRb1']))
    data5.append((s3ad['indicKRb1']))
        
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='-', color='k', label='Baseline')
g2, = axes.plot(data2, linestyle='--', color='k', label='+5% shock')
g3, = axes.plot(data3, linestyle='-.', color='k', label='+15% shock')
g4, = axes.plot(data4, linestyle=':', color='k', label='+25% shock')
g5, = axes.plot(data5, dashes=[10, 5, 20, 5], color='k', label='+35% shock')

plt.legend(handles=[g1,g2,g3,g4,g5], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%

caption = '''
    Figure 3 : Evolution of the net value of investing households, relative to the scenario 
    without any activation of coco bonds, following an increase in the share of defaulted loans'''
    
data1 = list()
data2 = list()
data3 = list()
data4 = list()

for i in range(400, 2000):
    s3aa = scenar3aa.solutions[i]
    s3ba = scenar3ba.solutions[i]
    s3ab = scenar3ab.solutions[i]
    s3bb = scenar3bb.solutions[i]
    s3ac = scenar3ac.solutions[i]
    s3bc = scenar3bc.solutions[i]
    s3ad = scenar3ad.solutions[i]
    s3bd = scenar3bd.solutions[i]
    data1.append((s3aa['V_r']) / (s3ba['V_r']))
    data2.append((s3ab['V_r']) / (s3bb['V_r']))
    data3.append((s3ac['V_r']) / (s3bc['V_r']))
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g2, = axes.plot(data1, linestyle='--', color='k', label='+5% shock')
g3, = axes.plot(data2, linestyle='-.', color='k', label='+15% shock')
g4, = axes.plot(data3, linestyle=':', color='k', label='+25% shock')

plt.legend(handles=[g2,g3,g4], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%

caption = '''
    Figure 4 : Evolution of the disposable income of investing households, relative to 
    the scenario without any activation of coco bonds, following an increase in the share
    of defaulted loans'''
    
data1 = list()
data2 = list()
data3 = list()
data4 = list()

for i in range(400, 2000):
    s3aa = scenar3aa.solutions[i]
    s3ba = scenar3ba.solutions[i]
    s3ab = scenar3ab.solutions[i]
    s3bb = scenar3bb.solutions[i]
    s3ac = scenar3ac.solutions[i]
    s3bc = scenar3bc.solutions[i]
    s3ad = scenar3ad.solutions[i]
    s3bd = scenar3bd.solutions[i]
    data1.append((s3aa['YD_r']) / (s3ba['YD_r']))
    data2.append((s3ab['YD_r']) / (s3bb['YD_r']))
    data3.append((s3ac['YD_r']) / (s3bc['YD_r']))
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g2, = axes.plot(data1, linestyle='--', color='k', label='+5% shock')
g3, = axes.plot(data2, linestyle='-.', color='k', label='+15% shock')
g4, = axes.plot(data3, linestyle=':', color='k', label='+25% shock')

plt.legend(handles=[g2,g3,g4], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%

caption = '''
    Figure 5 : Evolution of the consumption of investing households, relative to the scenario without
    any activation of coco bonds, following an increase in the share of defaulted loans'''
    
data1 = list()
data2 = list()
data3 = list()
data4 = list()

for i in range(400, 2000):
    s3aa = scenar3aa.solutions[i]
    s3ba = scenar3ba.solutions[i]
    s3ab = scenar3ab.solutions[i]
    s3bb = scenar3bb.solutions[i]
    s3ac = scenar3ac.solutions[i]
    s3bc = scenar3bc.solutions[i]
    s3ad = scenar3ad.solutions[i]
    s3bd = scenar3bd.solutions[i]
    data1.append((s3aa['C_r']) / (s3ba['C_r']))
    data2.append((s3ab['C_r']) / (s3bb['C_r']))
    data3.append((s3ac['C_r']) / (s3bc['C_r']))
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g2, = axes.plot(data1, linestyle='--', color='k', label='+5% shock')
g3, = axes.plot(data2, linestyle='-.', color='k', label='+15% shock')
g4, = axes.plot(data3, linestyle=':', color='k', label='+25% shock')

plt.legend(handles=[g2,g3,g4], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%

caption = '''
    Figure 6 : Evolution of the net value of firms, relative to the scenario 
    without any activation of coco bonds, following an increase in the share of defaulted loans'''
    
data1 = list()
data2 = list()
data3 = list()
data4 = list()

for i in range(400, 2000):
    s3aa = scenar3aa.solutions[i]
    s3ba = scenar3ba.solutions[i]
    s3ab = scenar3ab.solutions[i]
    s3bb = scenar3bb.solutions[i]
    s3ac = scenar3ac.solutions[i]
    s3bc = scenar3bc.solutions[i]
    s3ad = scenar3ad.solutions[i]
    s3bd = scenar3bd.solutions[i]
    data1.append((s3aa['V_f']) / (s3ba['V_f']))
    data2.append((s3ab['V_f']) / (s3bb['V_f']))
    data3.append((s3ac['V_f']) / (s3bc['V_f']))
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g2, = axes.plot(data1, linestyle='--', color='k', label='+5% shock')
g3, = axes.plot(data2, linestyle='-.', color='k', label='+15% shock')
g4, = axes.plot(data3, linestyle=':', color='k', label='+25% shock')

plt.legend(handles=[g2,g3,g4], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);


#%%

caption = '''
    Figure 7 : Evolution of firms' investment', relative to the scenario 
    without any activation of coco bonds, following an increase in the share of defaulted loans'''
    
data1 = list()
data2 = list()
data3 = list()
data4 = list()

for i in range(400, 2000):
    s3aa = scenar3aa.solutions[i]
    s3ba = scenar3ba.solutions[i]
    s3ab = scenar3ab.solutions[i]
    s3bb = scenar3bb.solutions[i]
    s3ac = scenar3ac.solutions[i]
    s3bc = scenar3bc.solutions[i]
    s3ad = scenar3ad.solutions[i]
    s3bd = scenar3bd.solutions[i]
    data1.append((s3aa['INV']) / (s3ba['INV']))
    data2.append((s3ab['INV']) / (s3bb['INV']))
    data3.append((s3ac['INV']) / (s3bc['INV']))
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g2, = axes.plot(data1, linestyle='--', color='k', label='+5% shock')
g3, = axes.plot(data2, linestyle='-.', color='k', label='+15% shock')
g4, = axes.plot(data3, linestyle=':', color='k', label='+25% shock')

plt.legend(handles=[g2,g3,g4], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%

caption = '''
    Figure 8 : Evolution of the wage bill of working households following an increase in defaulted loans
    in both crisis scenario (with and without activation of coco bonds)'''
    
data1 = list()
data2 = list()
data3 = list()
data4 = list()

for i in range(400, 2000):
    s3aa = scenar3aa.solutions[i]
    s3ba = scenar3ba.solutions[i]
    s3ab = scenar3ab.solutions[i]
    s3bb = scenar3bb.solutions[i]
    s3ac = scenar3ac.solutions[i]
    s3bc = scenar3bc.solutions[i]
    s3ad = scenar3ad.solutions[i]
    s3bd = scenar3bd.solutions[i]
    data1.append((s3aa['WB']) / (s3ba['WB']))
    data2.append((s3ab['WB']) / (s3bb['WB']))
    data3.append((s3ac['WB']) / (s3bc['WB']))
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g2, = axes.plot(data1, linestyle='--', color='k', label='+5% shock')
g3, = axes.plot(data2, linestyle='-.', color='k', label='+15% shock')
g4, = axes.plot(data3, linestyle=':', color='k', label='+25% shock')

plt.legend(handles=[g2,g3,g4], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%

caption = '''
    Figure 9 : Evolution of the consumption of working households, relative to the scenario without
    any activation of coco bonds, following an increase in the share of defaulted loans'''
    
data1 = list()
data2 = list()
data3 = list()
data4 = list()

for i in range(400, 2000):
    s3aa = scenar3aa.solutions[i]
    s3ba = scenar3ba.solutions[i]
    s3ab = scenar3ab.solutions[i]
    s3bb = scenar3bb.solutions[i]
    s3ac = scenar3ac.solutions[i]
    s3bc = scenar3bc.solutions[i]
    s3ad = scenar3ad.solutions[i]
    s3bd = scenar3bd.solutions[i]
    data1.append((s3aa['C_w']) / (s3ba['C_w']))
    data2.append((s3ab['C_w']) / (s3bb['C_w']))
    data3.append((s3ac['C_w']) / (s3bc['C_w']))
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g2, = axes.plot(data1, linestyle='--', color='k', label='+5% shock')
g3, = axes.plot(data2, linestyle='-.', color='k', label='+15% shock')
g4, = axes.plot(data3, linestyle=':', color='k', label='+25% shock')

plt.legend(handles=[g2,g3,g4], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%

caption = '''
    Figure 10 : Evolution of the net value of retails banks following an increase in defaulted loans
    in both crisis scenario (with and without activation of coco bonds)'''
    
data1 = list()
data2 = list()
data3 = list()
data4 = list()

for i in range(400, 2000):
    s3aa = scenar3aa.solutions[i]
    s3ba = scenar3ba.solutions[i]
    s3ab = scenar3ab.solutions[i]
    s3bb = scenar3bb.solutions[i]
    s3ac = scenar3ac.solutions[i]
    s3bc = scenar3bc.solutions[i]
    s3ad = scenar3ad.solutions[i]
    s3bd = scenar3bd.solutions[i]
    data1.append((s3aa['V_b1']) / (s3ba['V_b1']))
    data2.append((s3ab['V_b1']) / (s3bb['V_b1']))
    data3.append((s3ac['V_b1']) / (s3bc['V_b1']))
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g2, = axes.plot(data1, linestyle='--', color='k', label='+5% shock')
g3, = axes.plot(data2, linestyle='-.', color='k', label='+15% shock')
g4, = axes.plot(data3, linestyle=':', color='k', label='+25% shock')

plt.legend(handles=[g2,g3,g4], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%

caption = '''
    Figure 11 : Evolution of the bank debt to private debt ratio relative to 
    the scenario without any activation of coco bonds, following an increase in the share
    of defaulted loans'''
    
data1 = list()
data2 = list()
data3 = list()
data4 = list()

for i in range(400, 2000):
    s3aa = scenar3aa.solutions[i]
    s3ba = scenar3ba.solutions[i]
    s3ab = scenar3ab.solutions[i]
    s3bb = scenar3bb.solutions[i]
    s3ac = scenar3ac.solutions[i]
    s3bc = scenar3bc.solutions[i]
    s3ad = scenar3ad.solutions[i]
    s3bd = scenar3bd.solutions[i]
    data1.append((s3aa['bank_to_private']) / (s3ba['bank_to_private']))
    data2.append((s3ab['bank_to_private']) / (s3bb['bank_to_private']))
    data3.append((s3ac['bank_to_private']) / (s3bc['bank_to_private']))
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g2, = axes.plot(data1, linestyle='--', color='k', label='+5% shock')
g3, = axes.plot(data2, linestyle='-.', color='k', label='+15% shock')
g4, = axes.plot(data3, linestyle=':', color='k', label='+25% shock')

plt.legend(handles=[g2,g3,g4], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%

caption = '''
    Figure 12 : Evolution of the bank debt to public debt ratio relative to 
    the scenario without any activation of coco bonds, following an increase in the share
    of defaulted loans'''
    
data1 = list()
data2 = list()
data3 = list()
data4 = list()

for i in range(400, 2000):
    s3aa = scenar3aa.solutions[i]
    s3ba = scenar3ba.solutions[i]
    s3ab = scenar3ab.solutions[i]
    s3bb = scenar3bb.solutions[i]
    s3ac = scenar3ac.solutions[i]
    s3bc = scenar3bc.solutions[i]
    s3ad = scenar3ad.solutions[i]
    s3bd = scenar3bd.solutions[i]
    data1.append((s3aa['bank_to_public']) / (s3ba['bank_to_public']))
    data2.append((s3ab['bank_to_public']) / (s3bb['bank_to_public']))
    data3.append((s3ac['bank_to_public']) / (s3bc['bank_to_public']))
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g2, = axes.plot(data1, linestyle='--', color='k', label='+5% shock')
g3, = axes.plot(data2, linestyle='-.', color='k', label='+15% shock')
g4, = axes.plot(data3, linestyle=':', color='k', label='+25% shock')

plt.legend(handles=[g2,g3,g4], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%

caption = '''
    Figure 13 : State of the bailout trigger following an increase in defaulted loans 
    (1 = bailout ; 0 = no bailout)'''
    
data1 = list()
data2 = list()
data3 = list()

for i in range(440, 480):
    s3aa = scenar3aa.solutions[i]
    s3ba = scenar3ba.solutions[i]
    s3ab = scenar3ab.solutions[i]
    s3bb = scenar3bb.solutions[i]
    s3ac = scenar3ac.solutions[i]
    s3bc = scenar3bc.solutions[i]
    s3ad = scenar3ad.solutions[i]
    s3bd = scenar3bd.solutions[i]
    base = baseline2.solutions[i]
    data1.append((base['indicBO']))
    data2.append((s3ad['indicBO']))    
    data3.append((s3bd['indicBO']))
       
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='-', color='k', label='Baseline')
g2, = axes.plot(data2, linestyle='--', color='k', label='+35% shock, with CoCos')
g3, = axes.plot(data3, linestyle='-.', color='k', label='+35% shock, without CoCos')

plt.legend(handles=[g1,g2,g3], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%

caption = '''
    Figure 14 : Evolution of retail bank bailout costs with and without
    bail-ins, following an increase in the share of defaulted loans'''
    
data1 = list()
data2 = list()
data3 = list()

for i in range(440, 480):
    s3aa = scenar3aa.solutions[i]
    s3ba = scenar3ba.solutions[i]
    s3ab = scenar3ab.solutions[i]
    s3bb = scenar3bb.solutions[i]
    s3ac = scenar3ac.solutions[i]
    s3bc = scenar3bc.solutions[i]
    s3ad = scenar3ad.solutions[i]
    s3bd = scenar3bd.solutions[i]
    base = baseline2.solutions[i]
    data1.append((base['BO_s']))
    data2.append((s3ad['BO_s']))    
    data3.append((s3bd['BO_s']))
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='-', color='k', label='Baseline')
g2, = axes.plot(data2, linestyle='--', color='k', label='+35% shock, with CoCos')
g3, = axes.plot(data3, linestyle='-.', color='k', label='+35% shock, without CoCos')

plt.legend(handles=[g1,g2,g3], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%

#INSTABILITY INDICATORS

data1 = list()
data2 = list()
data3 = list()
data4 = list()
data5 = list()
data6 = list()
data7 = list()
data8 = list()
data9 = list()
data10 = list()
data11 = list()
data12 = list()
data13 = list()
data14 = list()
data15 = list()
data16 = list()
data17 = list()
data18 = list()

for i in range(100, 1000):
    s3ac = scenar3ac.solutions[i]
    s3bc = scenar3bc.solutions[i]
    base = baseline.solutions[i]
    data1.append((s3ac['Ygrowth']))
    data2.append((s3bc['Ygrowth']))
    data3.append((base['Ygrowth']))
    data4.append((s3ac['Cgrowth']))
    data5.append((s3bc['Cgrowth']))
    data6.append((base['Cgrowth']))
    data7.append((s3ac['V_rgrowth']))
    data8.append((s3bc['V_rgrowth']))
    data9.append((base['V_rgrowth']))
    data10.append((s3ac['V_wgrowth']))
    data11.append((s3bc['V_wgrowth']))
    data12.append((base['V_wgrowth']))  
    data13.append((s3ac['V_fgrowth']))
    data14.append((s3bc['V_fgrowth']))
    data15.append((base['V_fgrowth']))
    data16.append((s3ac['V_b1growth']))
    data17.append((s3bc['V_b1growth']))
    data18.append((base['V_b1growth']))
    
#%%
import numpy as np
import pandas as pd

df = pd.DataFrame(data1)
df.head()

#GDP
print((np.std(data1))/(np.std(data2)))
#Consumption
print((np.std(data4))/(np.std(data5)))
#Net value of investor households
print((np.std(data7))/(np.std(data8)))
#Net value of worker households
print((np.std(data10))/(np.std(data11)))
#Net value of firms
print((np.std(data13))/(np.std(data14)))
#Net value of retail banks
print((np.std(data16))/(np.std(data17)))