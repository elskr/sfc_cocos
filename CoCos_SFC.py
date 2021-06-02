#%%

#INTRODUCTION

#%matplotlib inline

from __future__ import division
from pysolve.model import Model
from pysolve.utils import is_close,round_solution

from matplotlib import rcParams, cycler
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D

#MODEL


def create_kremer_model():
    model = Model()
    
    model.set_var_default(0)
    model.var('A_b1d', desc="demande effective en avances de la part des banques de depot")
    model.var('A_b1s', desc="avances de la BC offertes aux banques de detail")
    model.var('A_b2d', desc="demande effective en avances de la part de banques d investissement")
    model.var('A_b2s', desc="avances de la BC offertes aux banques d investissement")
    model.var('A_Nb1d', desc="demande notionnelle des banques de detail en avances de la banque centrale")
    model.var('A_Nb2d', desc="demande notionnelle des banques d investissement en avances de la banque centrale")
    model.var('B_b2d', desc="demande des banques d investissement en bons du tresor")
    model.var('B_b2h', desc="bons du tresor detenus par les banques d investissement")
    model.var('B_b2s', desc="offre de bons du tresor a destination des banques d investissement")
    model.var('B_fd', desc="demande des firmes en bons du tresor")
    model.var('B_fh', desc="bons du tresor detenus par les firmes")
    model.var('B_fs', desc="offre de bons du tresor a destination des firmes")
    model.var('B_rd', desc="demande de Bons du Tresor des menages investisseurs")
    model.var('B_rh', desc="Bons du Tresor detenus par les menages investisseurs")
    model.var('B_rs', desc="offre de bons du tresor a destination des menages investisseurs")
    model.var('B_s', desc="offre de Bons du Tresor")
    model.var('BCO1_fd', desc="demande des firmes en coco bonds emis par les banques de detail")
    model.var('BCO1_fh', desc="coco bonds emis par les banques de detail detenus par les firmes")
    model.var('BCO1_fs', desc="coco bonds emis par les banques de detail a destination des firmes")
    model.var('BCO1_rd', desc="demande des menages investisseurs en coco bonds emis par les banques de detail")
    model.var('BCO1_rh', desc="coco bonds emis par les banques de detail detenus par les menages investisseurs")
    model.var('BCO1_rs', desc="coco bonds emis par les banques de detail a destination des menages investisseurs")
    model.var('BCO1_s', desc="offre de coco bonds emis par les banques de detail")
    model.var('BCO1_sN', desc="offre notionnelle")
    model.var('BCO2_fd', desc="demande des firmes en coco bonds emis par les banques d investissement")
    model.var('BCO2_fh', desc="coco bonds emis par les banques d investissement detenus par les firmes")
    model.var('BCO2_fs', desc="coco bonds emis par les banques d investissement a destination des firmes")
    model.var('BCO2_rd', desc="demande des menages investisseurs en coco bonds emis par les banques d investissement")
    model.var('BCO2_rh', desc="coco bonds emis par les banques d investissement detenus par les menages investisseurs")
    model.var('BCO2_rs', desc="coco bonds emis par les banques d investissement a destination des menages investisseurs")
    model.var('BCO2_s', desc="offre de coco bonds emis par les banques d investissement")
    model.var('BCO2_sN', desc="offre notionnelle")
    model.var('BUR_w', desc="poids de la dette des menages")
    model.var('c_r', desc="consommation reelle des menages investisseurs")
    model.var('C_r', desc="consommation nominale des menages investisseurs")
    model.var('C_w', desc="consommation nominale des menages travailleurs")
    model.var('c_w', desc="consommation reelle des menages travailleurs")
    model.var('CARb1', desc="capital adequacy ratio des banques de detail")
    model.var('CG_b2', desc="gains en capital des banques d investissement")
    model.var('CG_f', desc="gains en capital des firmes")
    model.var('CG_r', desc="gains en capital des menages investisseurs")
    model.var('D_rd', desc="demande de depots a vue des menages investisseurs")
    model.var('D_rh', desc="depots a vue detenus par les menages investisseurs")
    model.var('D_rs', desc="offre de depots a vue a destination des menages investisseurs")
    model.var('D_s', desc="offre total de depots a vue")
    model.var('D_wd', desc="demande de depots a vue des menages travailleurs")
    model.var('D_wh', desc="depots a vue detenus par les menages travailleurs")
    model.var('D_ws', desc="offre de depots a vue a destination des menages travailleurs")
    model.var('e_b2d', desc="demande des banques d investissement en actions d entreprises")
    model.var('e_b2h', desc="actions d entreprises detenus par les banques d investissement")
    model.var('e_b2s', desc="offre d actions d entreprises a destination des banques d investissement")
    model.var('e_rd', desc="demande en actions d entrerprises des menages investisseurs")
    model.var('e_rh', desc="actions d entreprises detenues par les menages investisseurs")
    model.var('e_rs', desc="offre d actions d entreprises a destination des menages investisseurs")
    model.var('e_s', desc="offre d actions emises par les firmes")
    model.var('ER', desc="taux d emploi")
    model.var('eta', desc="ratio nouveaux emprunts - revenu personnel")
    model.var('F_b1', desc="profits des banques de detail")
    model.var('F_b2', desc="profits des banques d investissement")
    model.var('F_cb', desc="profits de la banque centrale")
    model.var('F_f', desc="profits realises par les firmes")
    model.var('FD_b1', desc="total des profits redistribues par les banques de detail")
    model.var('FD_b2', desc="total des profits redistribues par les banque d investissement ")
    model.var('FD_b2f', desc="profits redistribues par les firmes a destination des banques d investissement")
    model.var('FD_f', desc="profits totaux redistribues par les firmes")
    model.var('FD_fb1', desc="profits distribues par les banques de detail a destination des firmes")
    model.var('FD_fb2', desc="profits distribues par les banques d investissement a destination des firmes")
    model.var('FD_rf', desc="profits redistribues par les firmes a destination des menages investisseurs")
    model.var('FD_rb1', desc="profits distribues par les banques de detail a destination des menages investisseurs")
    model.var('FD_rb2', desc="profits distribues par les banques d investissement a destination des menages investisseurs")
    model.var('FU_b1', desc="profits retenus des banques de detail")
    model.var('FU_b2', desc="profits retenus des banques d investissement")
    model.var('FU_f', desc="profits retenus par les firmes")
    model.var('G', desc="depenses publiques nominales")
    model.var('g', desc="depenses publiques reelles")
    model.var('GD', desc="dette publique nominale en tant que somme des deficits passes")
    model.var('GL_wd', desc="montant brut de nouveaux emprunts demande par les menages traailleurs")
    model.var('gr_k', desc="croissance du stock reel de capital des firmes")
    model.var('HPM_b1d', desc="reserve requirements des banques de detail")
    model.var('HPM_b1s', desc="cash offert aux banques de detail")
    model.var('HPM_b2d', desc="reserve requirements des banques d investissement")
    model.var('HPM_b2s', desc="cash offert aux banques d investissement")
    model.var('INV', desc="investissement brut nominal des firmes")
    model.var('inv', desc="investissement brut reel")
    model.var('IN', desc="inventaires des firmes valorises a cout courant")
    model.var('ink', desc="inventaires reels effectifs des firmes")
    model.var('ine', desc="cible d inventaires a court terme des firmes")
    model.var('inT', desc="cible d inventaires a long terme des firmes")
    model.var('indicKRb1', desc="condition")
    model.var('indicKRb1bis', desc="condition")
    model.var('indicKRb2', desc="condition")
    model.var('indicKRb2bis', desc="condition")
    model.var('K', desc="stock nominal de capital fixe des firmes")
    model.var('k', desc="stock reel de capital des firmes")
    model.var('klim', desc="part de credit rationne")
    model.var('KR_b1', desc="ratio de fonds propres des banques de detail")
    model.var('KR_b2', desc="ratio de fonds propres des banques d investissement")
    model.var('l', desc="ratio de levier des firmes")
    model.var('L_fd', desc="demande de prets des firmes")
    model.var('L_fs', desc="credits accordes aux firmes")
    model.var('L_wd', desc="demande d emprunts des menages travailleurs")
    model.var('L_ws', desc="credits accordes aux menages travailleurs")
    model.var('LEV_w', desc="ratio de levier des menages travailleurs")
    model.var('N', desc="emploi effectif")
    model.var('NT', desc="emploi desire")
    model.var('NHUC', desc="cout unitaire normal historique des firmes")
    model.var('NL_wd', desc="montant nominal  net de nouveaux emprunts demande par les menages travailleurs")
    model.var('NL_ws', desc="offre nette nominale de credit a destination des menages travailleurs")
    model.var('nl_ws', desc="offre nette reelle de credit a destination des menages travailleurs")
    model.var('nl_wse', desc="offre nette relle de credit anticipee par les menages travailleurs")
    model.var('NPLW', desc="defauts sur prets des menages travailleurs")
    model.var('nplw', desc="part de defauts sur prets")
    model.var('NUC', desc="cout unitaire normal des firmes")
    model.var('OFB1_rh', desc="coco equities emises par les banques de depot detenues par les menages investisseurs")
    model.var('OFB1_fh', desc="coco equities emises par les banques de depot detenues par les firmes")
    model.var('OFB1_s', desc="offre totale de coco equities de la part des banques de depot")
    model.var('OFB2_rh', desc="coco equities emises par les banques d investissement detenues par les menages investisseurs")
    model.var('OFB2_fh', desc="coco equities emises par les banques d investissement detenues par les firmes")
    model.var('OFB2_s', desc="offre totale de coco equities de la part des banques d inestissement")
    model.var('omegaT', desc="salaire reel souhaite par les travailleurs au moment des negociations")
    model.var('p', desc="prix fixe par les firmes")
    model.var('pbco1', desc="prix des coco bonds emis par les banques de detail")
    model.var('pbco2', desc=": prix des coco bonds emis par les banques d investissement")
    model.var('pe', desc="prix des actions d entreprises")
    model.var('PE', desc="price earnings ratio")
    model.var('PI', desc="taux d inflation")
    model.var('pr', desc="productivite du travail")
    model.var('PSBR', desc="deficit public nominal")
    model.var('r_BCO1', desc="taux de rendement des coco bonds emis par les banques de detail")
    model.var('r_BCO2', desc="taux de rendement des coco bonds emis par les banques d investissement")
    model.var('r_cf', desc="ratio des flux de tresorerie des firmes")
    model.var('r_d', desc="taux sur les depots a vue")
    model.var('r_fTOT', desc="interets sur titres des firmes")
    model.var('r_K', desc="taux de rendement des actions des firmes")
    model.var('r_l', desc="taux sur les prets")
    model.var('r_q', desc="Q de Tobin")
    model.var('r_td', desc="taux sur les depots a terme aupres des banques d investissement")
    model.var('REP_w', desc="remboursement de leurs emprunts par les menages travailleurs")
    model.var('rr_cf', desc="ratio des flux reels de tresorerie des firmes")
    model.var('rr_l', desc="taux  d interet reel sur les emprunts des firmes")
    model.var('rr_q', desc="Q de Tobin reel")
    model.var('S', desc="ventes nominales effectives des firmes")
    model.var('s', desc="ventes reeles effectives des firmes")
    model.var('se', desc="ventes reelles anticipees des firmes")
    model.var('T', desc="taxes sur le revenu totales collectees par le gouvernement")
    model.var('T_r', desc="taxes sur le revenu des menages investisseurs")
    model.var('T_w', desc="taxes sur le revenu des menages travailleurs")
    model.var('TD_rd', desc="demande de depots a terme des menages investisseurs aupres des banques d investissement")
    model.var('TD_rh', desc="depots a terme aupres des banques d investissement detenus par les menages investisseurs")
    model.var('TD_rs', desc="offre des banques d investissement en depots a terme a destination des menages investisseurs")
    model.var('u', desc="utilisation des capacites de production par les firmes")
    model.var('UC', desc="cout unitaire effectif des firmes")
    model.var('V_b1', desc="valeur nette des banques de detail")
    model.var('V_b2', desc="valeur nette des banques d investissement")
    model.var('V_f', desc="valeur nette des firmes")
    model.var('V_r', desc="richesse nominale des menages investisseurs")
    model.var('v_r', desc="richesse reelle des menages investisseurs")
    model.var('V_w', desc="richesse nominale des menages travailleurs")
    model.var('v_w', desc="richesse reelle des menages travailleurs")
    model.var('Vfma_b2', desc="richesse financiere nette investissable des banques d investissement")
    model.var('Vfma_r', desc="richesse financiere nette investissable des menages investisseurs")
    model.var('Vfma_w', desc="richesse financiere nette investissable des menages travailleurs")
    model.var('Vfma_f', desc="richesse financiere nette investissable des firmes")
    model.var('W', desc="salaire nominal")
    model.var('WB', desc="masse salariale nominale")
    model.var('y', desc="production reelle des firmes")
    model.var('Y', desc="PIB nominal")
    model.var('YD_r', desc="revenu nominal disponible des menages investisseurs")
    model.var('yd_r', desc="revenu reel disponible des menages investisseurs")
    model.var('yd_re', desc="revenu reel disponible anticipe des menages investisseurs")
    model.var('YD_w', desc="revenu nominal disponible des menages travailleurs")
    model.var('yd_w', desc="revenu reel disponible")
    model.var('yd_we', desc="revenu reel disponible anticipe des menages travailleurs")
    model.var('YDHS_r', desc="revenu nominal disponible a la Haig-Simons des menages investisseurs")
    model.var('YP_r', desc="revenu nominal des menages investisseurs")
    model.var('YP_w', desc="revenu nominal des menages travailleurs")
    model.var('z5', desc="condition")
    model.var('z6', desc="condition")
    model.var('pemean', desc = "pe")
    model.var('pevar', desc = "pe")
    model.var('pestd', desc = "pe")
    model.var('pegrowth', desc = "pe")
    model.var('Ygrowth', desc = "taux de croissance de la production")
    model.var('Cgrowth', desc = "taux de croissance de la consommation totale")
    model.var('V_rgrowth', desc = "taux de croissance de la valeur nette des menages investisseurs")
    model.var('V_wgrowth', desc = "taux de croissance de la valeur nette des menages travailleurs")
    model.var('V_fgrowth', desc = "taux de croissance de la valeur nette des firmes")
    model.var('V_b1growth', desc = "taux de croissance de la valeur nette des banques de detail")
    model.var('V_b2growth', desc = "taux de croissance de la valeur nette des banques d investissement")
    
    
    model.set_param_default(0)
    model.param('alpha1', desc="propension a consommer en fonction du revenu")
    model.param('alpha2', desc="propension a consommer en fonction de l epargne")
    model.param('beta', desc="parametre formation des anticipations des ventes reelles")
    model.param('CARTb1', desc="capital adequacy ratio cible des banques de detail")
    model.param('chi1', desc="spread taux d interet sur pret par rapport a taux sur avances")
    model.param('chi2', desc="spread taux d interet sur depots a vue par rapport a taux sur avances")
    model.param('chi3', desc="spread taux d interet sur depots a terme aupres des banques d investissement par rapport a taux sur avances")
    model.param('delta', desc="taux de depreciation du capital fixe")
    model.param('deltarep', desc="ratio remboursement d emprunts – stock d emprunts")
    model.param('epsilon', desc="parametre formation des anticipations sur le revenu reel disponible")
    model.param('epsilon1', desc="parametre formation des anticipations des menages travailleurs sur l offre nette de credit a leur destination")
    model.param('epsilon20', desc="parametre demande des banques d investissement en actions d entreprises")
    model.param('epsilon21', desc="parametre demande des banques d investissement en actions d entreprises")
    model.param('epsilon22', desc="parametre demande des banques d investissement en actions d entreprises")
    model.param('eta0', desc="parametre constant ratio nouveaux emprunts – revenu personnel")
    model.param('etaw', desc="relation entre le ratio de nouveaux emprunts – revenu personnel et le taux d interet sur ces emprunts")
    model.param('gamma', desc="vitesse d ajustement des inventaires à leur cible")
    model.param('gamma0', desc="composante exogene dans la croissance du stock reel de capital")
    model.param('gamma1', desc="relation entre le taux d utilisation des capacites de production et la croissance du stock de capital")
    model.param('gamma2', desc="relation entre le taux d interet reel et la croissance du stock reel de capital")
    model.param('gamma3', desc="relation entre les flux de tresorerie et la croissance du stock reel de capital")
    model.param('gamma4', desc="relation entre le Q de Tobin et la croissance du stock reel de capital")
    model.param('grg', desc="croissance des depenses publiques")
    model.param('grpr', desc="croissance de la productivite du travail")
    model.param('klim0', desc="parametre rationnement credit - composante exogene")
    model.param('klim1', desc="lien entre rationnement credit et levier menages")
    model.param('klim2', desc="lien entre rationnement credit et cible de capital adequacy ratio")
    model.param('klim3', desc="lien entre rationnement credit et poids de la dette des menages")
    model.param('klim4', desc="lien entre rationnement credit et proportion de defauts sur prets") 
    model.param('KRT1', desc="ratio trigger banques de detail")
    model.param('KRT2', desc="ratio trigger banques d investissement")
    model.param('lambda20', desc="parametre demande de depots a terme des menages aupres des banques d investissement")
    model.param('lambda21', desc="parametre demande de depots a terme des menages aupres des banques d investissement")
    model.param('lambda22', desc="parametre demande de depots a terme des menages aupres des banques d investissement")
    model.param('lambda23', desc="parametre demande de depots a terme des menages aupres des banques d investissement")
    model.param('lambda24', desc="parametre demande de depots a terme des menages aupres des banques d investissement")
    model.param('lambda25', desc="parametre demande de depots a terme des menages aupres des banques d investissement")
    model.param('lambda26', desc="parametre demande de depots a terme des menages aupres des banques d investissement")
    model.param('lambda30', desc="parametre demande des menages en bons du Tresor")
    model.param('lambda31', desc="parametre demande des menages en bons du Tresor")
    model.param('lambda32', desc="parametre demande des menages en bons du Tresor")
    model.param('lambda33', desc="parametre demande des menages en bons du Tresor")
    model.param('lambda34', desc="parametre demande des menages en bons du Tresor")
    model.param('lambda35', desc="parametre demande des menages en bons du Tresor")
    model.param('lambda36', desc="parametre demande des menages en bons du Tresor")
    model.param('lambda40', desc="parametre demande des menages en actions d entreprises")
    model.param('lambda41', desc="parametre demande des menages en actions d entreprises")
    model.param('lambda42', desc="parametre demande des menages en actions d entreprises")
    model.param('lambda43', desc="parametre demande des menages en actions d entreprises")
    model.param('lambda44', desc="parametre demande des menages en actions d entreprises")
    model.param('lambda45', desc="parametre demande des menages en actions d entreprises")
    model.param('lambda46', desc="parametre demande des menages en actions d entreprises")
    model.param('lambda50', desc="parametre demande des menages en cocos emis par les banques de depot")
    model.param('lambda51', desc="parametre demande des menages en cocos emis par les banques de depot")
    model.param('lambda52', desc="parametre demande des menages en cocos emis par les banques de depot")
    model.param('lambda53', desc="parametre demande des menages en cocos emis par les banques de depot")
    model.param('lambda54', desc="parametre demande des menages en cocos emis par les banques de depot")
    model.param('lambda55', desc="parametre demande des menages en cocos emis par les banques de depot")
    model.param('lambda56', desc="parametre demande des menages en cocos emis par les banques de depot")
    model.param('lambda60', desc="parametre demande des menages en cocos emis par les banques d investissement")
    model.param('lambda61', desc="parametre demande des menages en cocos emis par les banques d investissement")
    model.param('lambda62', desc="parametre demande des menages en cocos emis par les banques d investissement")
    model.param('lambda63', desc="parametre demande des menages en cocos emis par les banques d investissement")
    model.param('lambda64', desc="parametre demande des menages en cocos emis par les banques d investissement")
    model.param('lambda65', desc="parametre demande des menages en cocos emis par les banques d investissement")
    model.param('lambda66', desc="parametre demande des menages en cocos emis par les banques d investissement")
    model.param('N_fe', desc="plein emploi")
    model.param('nplw0', desc="part de defauts sur prets - composante exogene")
    model.param('nplw1', desc="relation entre part defauts sur prets et poids de la dette des menages")
    model.param('nplw2', desc="relation entre part defauts sur prets et disponibilite du credit")
    model.param('omega0', desc="parametre influençant le salaire cible")
    model.param('omega1', desc="parametre influençant le salaire cible en lien avec la productivite du travail")
    model.param('omega2', desc="parametre influençant le salaire cible en lien avec le taux d emploi")
    model.param('omega3', desc="vitesse d ajustement du salaire a sa cible")
    model.param('omega4', desc="vitesse  d ajustement de l emploi a sa cible")
    model.param('phi', desc="mark-up effectif")
    model.param('pitarget', desc="taux d inflation cible de la banque centrale")    
    model.param('psiD', desc="ratio dividendes – profits bruts")
    model.param('psiU', desc="ratio profits retenus – investissement")       
    model.param('rho1', desc="parametre reserve requirements banques de depot")    
    model.param('rho2', desc="parametre reserve requirements banques d investissement")
    model.param('sigmaN', desc="parametre determinant le cout historique normal unitaire")    
    model.param('sigmaT', desc="ratio inventaires cibles – ventes")
    model.param('sigmab1', desc="part de profits redistribues par les banques de detail")
    model.param('sigmab2', desc="part de profits redistribues par les banques d investissement")
    model.param('sigmafb1', desc="part de cocos emis par les banques de detail a destination des firmes")
    model.param('sigmarb1', desc="part de cocos emis par les banques de detail a destination des menages investisseurs")
    model.param('sigmarb2', desc="part de cocos emis par les banques d investissement a destination des menages investisseurs")
    model.param('tau20', desc="parametre demande des firmes en cocos emis par les banques de depot")    
    model.param('tau21', desc="parametre demande des firmes en cocos emis par les banques de depot")
    model.param('tau22', desc="parametre demande des firmes en cocos emis par les banques de depot")
    model.param('tau23', desc="parametre demande des firmes en cocos emis par les banques de depot")
    model.param('tau30', desc="parametre demande des firmes en cocos emis par les banques d investissement")    
    model.param('tau31', desc="parametre demande des firmes en cocos emis par les banques d investissement")
    model.param('tau32', desc="parametre demande des firmes en cocos emis par les banques d investissement")
    model.param('tau33', desc="parametre demande des firmes en cocos emis par les banques d investissement")
    model.param('tauxconvb1', desc="taux de conversion coco bonds - coco equities pour les banques de detail")
    model.param('tauxconvb2', desc="taux de conversion coco bonds - coco equities pour les banques d investissement")    
    model.param('theta', desc="taux de taxation sur le revenu des memages")        
    model.param('upsilon', desc="part des actions emises par les firmes a destination des menages investisseurs")
    model.param('z1', desc="relation entre la dette des banques de detail et leur emission de coco bonds")
    model.param('z2', desc="relation entre la dette des banques d investissement et leur emission de coco bonds")
    model.param('zeta', desc="part de profits retenus consacree à l investissement financier")    
    model.param('r_a', desc="taux d interet sur les avances")
    model.param('r_b', desc="taux d interet sur les bons du tresor")

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
    model.add('nplw = 0.1 + nplw0 + nplw1 * BUR_w(-1) - nplw2 * klim(-1)')
    model.add('Vfma_w = V_w + L_ws')
    model.add('D_wd = Vfma_w')
    model.add('D_ws = D_wd')
    model.add('D_wh = D_ws')

    
    #Investor-households' equations
    model.add('YP_r = r_d(-1) * D_rh(-1) + r_td(-1) * TD_rh(-1) + indicKRb1 * BCO1_rh(-1) + indicKRb2 * BCO2_rh(-1) + r_b(-1) * B_rh(-1) + FD_rf + FD_rb1 + FD_rb2')
    model.add('T_r = theta * YP_r')
    model.add('YD_r = YP_r + CG_r - T_r')
    model.add('CG_r = (pbco1 - pbco1(-1)) * indicKRb1 * BCO1_rh(-1) + (pbco2 - pbco2(-1)) * indicKRb2 * BCO2_rh(-1) + (pe - pe(-1)) * e_rh(-1)')
    model.add('YDHS_r = YD_r')
    model.add('V_r - V_r(-1) = YDHS_r - C_r + (indicKRb1 - 1) * BCO1_rh(-1) + (indicKRb2 - 1) * BCO2_rh(-1)')
    model.add('v_r = V_r / p')
    model.add('c_r = alpha1 * yd_re + alpha2 * v_r(-1)')
    model.add('C_r = p * c_r')
    model.add('yd_r = YD_r / p')
    model.add('yd_re = epsilon * yd_r + (1 - epsilon) * yd_r(-1)')
    model.add('Vfma_r = V_r - (OFB1_rh + OFB2_rh)')
    model.add('TD_rd = Vfma_r(-1) * (lambda20 - lambda21 * r_d + lambda22 * r_td - lambda23 * r_b - lambda24 * r_K - lambda25 * indicKRb1 * r_BCO1 - lambda26 * indicKRb2 * r_BCO2)')
    model.add('B_rd = Vfma_r(-1) * (lambda30 - lambda31 * r_d - lambda32 * r_td + lambda33 * r_b - lambda34 * r_K - lambda35 * indicKRb1 * r_BCO1 - lambda36 * indicKRb2 * r_BCO2)')
    model.add('D_rd = Vfma_r - TD_rs - B_rs - pe * e_rs - pbco1 * BCO1_rs - pbco2 * BCO2_rs')
    model.add('e_rd = e_rs')
    model.add('B_rs = B_rd')
    model.add('B_rh = B_rs')
    model.add('e_rh = e_rs')
    model.add('D_rs = D_rd')
    model.add('D_rh = D_rs')
    model.add('OFB1_rh = OFB1_rh(-1) + tauxconvb1 * BCO1_rh(-1) * indicKRb1bis')
    model.add('OFB2_rh = OFB2_rh(-1) + tauxconvb2 * BCO2_rh(-1) * indicKRb2bis')

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
    model.add('F_f = S - WB + (IN - IN(-1)) - r_l(-1) * IN(-1) + r_fTOT + CG_f + FD_fb1 + FD_fb2')    
    model.add('FD_f = psiD * F_f(-1)')
    model.add('FD_rf = upsilon * FD_f')    
    model.add('FD_b2f = (1 - upsilon) * FD_f')    
    model.add('FU_f = F_f - FD_f - r_l(-1) * (L_fd(-1) - IN(-1))')
    model.add('L_fd = L_fd(-1) + INV + (IN - IN(-1)) - (1 - zeta) * FU_f - (e_s - e_s(-1)) * pe')    
    model.add('e_s - e_s(-1) = (1 - psiU) * INV(-1) / pe')    
    model.add('r_K = FD_f / (e_s(-1) * pe(-1))')
    model.add('PE = pe * e_s(-1) / F_f')
    model.add('r_fTOT = r_b * B_fh(-1) + indicKRb1 * BCO1_fh(-1) + indicKRb2 * BCO2_fh(-1)')
    model.add('CG_f = BCO1_fh(-1) * (pbco1 - pbco1(-1)) * indicKRb1 + BCO2_fh(-1) * (pbco2 - pbco2(-1)) * indicKRb2')
    model.add('V_f = V_f(-1) + zeta * FU_f + (indicKRb1 - 1) * BCO1_fh(-1) + (indicKRb2 - 1) * BCO2_fh(-1)')
    model.add('Vfma_f = V_f - (OFB1_fh + OFB2_fh)')
    model.add('B_fd = V_f - pbco1 * indicKRb1 * BCO1_fs - pbco2 * indicKRb2 * BCO2_fs')
    model.add('e_rs = upsilon * e_s')
    model.add('e_b2s = e_s - e_rs')
    model.add('B_fs = B_fd')
    model.add('B_fh = B_fs')
    model.add('OFB1_fh = OFB1_fh(-1) + tauxconvb1 * BCO1_fh(-1) * indicKRb1bis')
    model.add('OFB2_fh = OFB2_fh(-1) + tauxconvb2 * BCO2_fh(-1) * indicKRb2bis')

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
    model.add('A_Nb1d = L_ws + L_fs + HPM_b1d - D_s - OFB1_s - pbco1 * indicKRb1 * BCO1_s - V_b1')
    model.add('z5 = if_true(A_Nb1d > 0)')
    model.add('A_b1d = z5 * A_Nb1d')
    model.add('A_b1s = A_b1d')
    model.add('F_b1 = r_l(-1) * (L_fs(-1) + L_ws(-1) - NPLW) - r_d(-1) * D_s(-1) - r_a(-1) * A_b1s(-1) - indicKRb1 * BCO1_s(-1)')
    model.add('r_l = r_a + chi1')
    model.add('r_d = r_a - chi2')
    model.add('V_b1 - V_b1(-1) = FU_b1 - NPLW  - (indicKRb1 - 1) * BCO1_s(-1)')
    model.add('FU_b1 = F_b1 - FD_b1')
    model.add('FD_b1 = indicKRb1bis * sigmab1 * F_b1(-1)')
    model.add('FD_rb1 = indicKRb1bis * sigmarb1 * FD_b1')
    model.add('FD_fb1 = indicKRb1bis * (FD_b1 - FD_rb1)')
    model.add('BCO1_s = indicKRb1 * BCO1_s(-1) + z1 * indicKRb1 * (D_s(-1) - D_s(-2)) / pbco1')
    model.add('BCO1_sN - BCO1_sN(-1) = z1 * (D_s(-1) - D_s(-2)) / pbco1')
    model.add('OFB1_s - OFB1_s(-1) = pbco1(-1) * BCO1_s(-1) * indicKRb1bis * tauxconvb1')
    model.add('KR_b1 = CARb1')
    model.add('r_BCO1 = indicKRb1 * (BCO1_s(-1) / (pbco1(-1) * BCO1_sN(-1)))')
    model.add('indicKRb1 = if_true(KR_b1(-1) > KRT1)')
    model.add('indicKRb1bis = 0')
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
    model.add('pemean = (pegrowth + pegrowth(-1) + pegrowth(-2) + pegrowth(-3) + pegrowth(-4)) / 4')
    model.add('pevar = ((pegrowth - pemean) * (pegrowth - pemean)) / 4')
    model.add('pestd = (pevar)**0.5')
    model.add('HPM_b2d = rho2 * TD_rs')
    model.add('HPM_b2s = HPM_b2d')
    model.add('A_Nb2d = HPM_b2d + B_b2d + pe * e_b2d - TD_rs - OFB2_s - indicKRb2 * pbco2 * BCO2_s - V_b2')
    model.add('z6 = if_true(A_Nb2d >0)')
    model.add('A_b2d = A_Nb2d * z6')
    model.add('A_b2s = A_b2d')
    model.add('F_b2 = FD_b2f + CG_b2 - r_td(-1) * TD_rs(-1) - indicKRb2 * BCO2_s(-1) + r_b(-1) * B_b2s(-1) - r_a(-1) * A_b2s(-1)')
    model.add('r_td = r_a - chi3')
    model.add('V_b2 - V_b2(-1) = FU_b2 - (indicKRb2 - 1) * BCO2_s(-1)')
    model.add('CG_b2 = e_b2h(-1) * (pe - pe(-1))')
    model.add('FU_b2 = F_b2 - FD_b2')
    model.add('FD_b2 = indicKRb2bis * sigmab2 * F_b2(-1)')
    model.add('FD_rb2 = indicKRb2bis * sigmarb2 * FD_b2')
    model.add('FD_fb2 = indicKRb2bis * (FD_b2 - FD_rb2)')
    model.add('Vfma_b2 = V_b2 - HPM_b2s')
    model.add('B_b2d = Vfma_b2 - pe * e_b2s')
    model.add('BCO2_s = indicKRb2 * BCO2_s(-1) + z2 * indicKRb2 * (TD_rs(-1) - TD_rs(-2)) / pbco2')
    model.add('BCO2_sN - BCO2_sN(-1) = z2 * (TD_rs(-1) - TD_rs(-2)) / pbco2')
    model.add('OFB2_s - OFB2_s(-1) = BCO2_s(-1) * indicKRb2bis * tauxconvb2')
    model.add('KR_b2 = pestd')
    model.add('r_BCO2 = indicKRb2 * (BCO2_s(-1) / (pbco2(-1) * BCO2_sN(-1)))')
    model.add('indicKRb2 = if_true(KR_b2(-1) < KRT2)')
    model.add('indicKRb2bis = 0')    
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
    model.add('pbco1 = ((Vfma_r(-1) * (lambda50 - lambda51 * r_d - lambda52 * r_td - lambda53 * r_b - lambda54 * r_K + lambda55 * indicKRb1 * r_BCO1 - lambda56 * indicKRb2 * r_BCO2)) + (Vfma_f(-1) * (tau20 - tau21 * r_b + tau22 * indicKRb1 * r_BCO1 - tau23 * indicKRb2 * r_BCO2))) / BCO1_sN')
    model.add('pbco2 = ((Vfma_r(-1) * (lambda60 - lambda61 * r_d - lambda62 * r_td - lambda63 * r_b - lambda64 * r_K - lambda65 * indicKRb1 * r_BCO1 + lambda66 * indicKRb2 * r_BCO2)) + (Vfma_f(-1) * (tau30 - tau31 * r_b - tau32 * indicKRb1 * r_BCO1 + tau33 * indicKRb2 * r_BCO2))) / BCO2_sN')
    model.add('pe = ((Vfma_r(-1) * (lambda40 - lambda41 * r_d - lambda42 * r_td - lambda43 * r_b + lambda44 * r_K - lambda45 * indicKRb1 * r_BCO1 - lambda46 * indicKRb2 * r_BCO2)) + (V_b2(-1) * (epsilon20 - epsilon21 * r_b + epsilon22 * r_K))) / e_s')
    
    #Taux de croissance
    model.add('Ygrowth = (Y - Y(-1)) / Y(-1)')
    model.add('Cgrowth = (C_w + C_r - C_w(-1) - C_r(-1)) / (C_w(-1) + C_r(-1))')
    model.add('V_rgrowth = (V_r - V_r(-1)) / V_r(-1)')
    model.add('V_wgrowth = (V_w - V_w(-1)) / V_w(-1)')
    model.add('V_fgrowth = (V_f - V_f(-1)) / V_f(-1)')
    model.add('V_b1growth = (V_b1 - V_b1(-1)) / V_b1(-1)')
    model.add('V_b2growth = (V_b2 - V_b2(-1)) / V_b2(-1)')
    
    return model


parameters = {'chi1': 0.01962,
             'chi2': 0.01,
             'chi3': 0.0019,
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
             'nplw0': 0.2,
             'nplw1': 0.25,
             'nplw2': 0.2,
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
             'sigmab1': 0.15255,
             'sigmab2': 0.15255,
             'sigmarb1': 1/2,
             'sigmarb2': 1/2,
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
             'tauxconvb1': 0.5,
             'tauxconvb2': 0.5,
             'theta': 0.22844,
             'upsilon': 1/2,
             'z1': 0.1,
             'z2': 0.1,
             'zeta': 0.9}

exogenous = [('grg', 0.03),
             ('grpr', 0.06),
             ('klim', 0.97),
             ('KRT1', -100000),
             ('KRT2', 100000),
             ('CARTb1', 0.1),
             ('pitarget', 0.02),
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
             ('r_l', 0.021921),
             ('r_d', 0.01301),
             ('r_td', 0.02111),
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
             ('BCO2_s', 511200),
             ('BCO2_sN', 511200),
             ('BCO2_rs', 255600),
             ('BCO2_rd', 'BCO2_rs'),
             ('BCO2_fs', 255600),
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
             ('Vfma_f', 2653950),
             ('V_r', 9653950),
             ('Vfma_r', 9592910),
             ('v_r', 1025760),
             ('V_w', 9653950),
             ('Vfma_w', 9653950),
             ('v_w', 9653950),
             ('indicKRb1', 1),
             ('indicKRb1bis', 0),
             ('indicKRb2', 1),
             ('indicKRb2bis', 0)]

#Baseline
baseline = create_kremer_model()
baseline.set_values(parameters)
baseline.set_values(exogenous)
baseline.set_values(variables)


for _ in range(2000):
    baseline.solve(iterations=2000, threshold=1e-6)
    

#%%
        
#SCENARIO 1Aa : hausse des défauts sur prêts (+40%) accordés aux ménages avec activation de coco bonds


scenar1aa = create_kremer_model()
scenar1aa.set_values(parameters)
scenar1aa.set_values(exogenous)
scenar1aa.set_values(variables)

for _ in range(40):
    scenar1aa.solve(iterations=1000, threshold=1e-6)

scenar1aa.set_values({'KRT1': 0.21})    
scenar1aa.set_values({'nplw0': 0.3})


for _ in range(10):
    scenar1aa.solve(iterations=1000, threshold=1e-6)
    
scenar1aa.set_values({'nplw0': 0.2})

for _ in range(950):
    scenar1aa.solve(iterations=1000, threshold=1e-6)
    
        
#SCENARIO 1Ab : hausse des défauts sur prêts (+60%) accordés aux ménages avec activation de coco bonds


scenar1ab = create_kremer_model()
scenar1ab.set_values(parameters)
scenar1ab.set_values(exogenous)
scenar1ab.set_values(variables)

for _ in range(40):
#for _ in range(50):
    scenar1ab.solve(iterations=1000, threshold=1e-6)

scenar1ab.set_values({'KRT1': 0.21})
scenar1ab.set_values({'nplw0': 0.45})


for _ in range(10):
    scenar1ab.solve(iterations=1000, threshold=1e-6)
    
scenar1ab.set_values({'nplw0': 0.2})

for _ in range(950):
    scenar1ab.solve(iterations=1000, threshold=1e-6)
    
        
#SCENARIO 1Ac : hausse des défauts sur prêts (+80%) accordés aux ménages avec activation de coco bonds


scenar1ac = create_kremer_model()
scenar1ac.set_values(parameters)
scenar1ac.set_values(exogenous)
scenar1ac.set_values(variables)

for _ in range(40):
    scenar1ac.solve(iterations=1000, threshold=1e-6)
    
scenar1ac.set_values({'KRT1': 0.21})
scenar1ac.set_values({'nplw0': 0.6})

for _ in range(10):
    scenar1ac.solve(iterations=1000, threshold=1e-6)
    
scenar1ac.set_values({'nplw0': 0.2})

for _ in range(950):
    scenar1ac.solve(iterations=1000, threshold=1e-6)
    
    
#SCENARIO 1Ba : hausse des défauts sur prêts (+40%) accordés aux ménages sans activation de cocobonds

scenar1ba = create_kremer_model()
scenar1ba.set_values(parameters)
scenar1ba.set_values(exogenous)
scenar1ba.set_values(variables)

scenar1ba.set_values({'KRT1': -100000})

for _ in range(40):
    scenar1ba.solve(iterations=1000, threshold=1e-6)
    
scenar1ba.set_values({'nplw0': 0.3})


for _ in range(10):
    scenar1ba.solve(iterations=1000, threshold=1e-6)
    
scenar1ba.set_values({'nplw0': 0.2})

for _ in range(950):
    scenar1ba.solve(iterations=1000, threshold=1e-6)


    
#SCENARIO 1Bb : hausse des défauts sur prêts (+60%) accordés aux ménages sans activation de cocobonds

scenar1bb = create_kremer_model()
scenar1bb.set_values(parameters)
scenar1bb.set_values(exogenous)
scenar1bb.set_values(variables)

scenar1bb.set_values({'KRT1': -100000})

for _ in range(40):
    scenar1bb.solve(iterations=1000, threshold=1e-6)
    
scenar1bb.set_values({'nplw0': 0.45})


for _ in range(10):
    scenar1bb.solve(iterations=1000, threshold=1e-6)
    
scenar1bb.set_values({'nplw0': 0.2})

for _ in range(950):
    scenar1bb.solve(iterations=1000, threshold=1e-6)


    
#SCENARIO 1Bc : hausse des défauts sur prêts (+80%) accordés aux ménages sans activation de cocobonds

scenar1bc = create_kremer_model()
scenar1bc.set_values(parameters)
scenar1bc.set_values(exogenous)
scenar1bc.set_values(variables)

scenar1bc.set_values({'KRT1': -100000})

for _ in range(40):
    scenar1bc.solve(iterations=1000, threshold=1e-6)
    
scenar1bc.set_values({'nplw0': 0.6})


for _ in range(10):
    scenar1bc.solve(iterations=1000, threshold=1e-6)
    
scenar1bc.set_values({'nplw0': 0.2})

for _ in range(950):
    scenar1bc.solve(iterations=1000, threshold=1e-6)


#%%
    
caption = '''
    Figure 1 : CAR of retail banks following an increase in defaulted loans'''

data1 = list()
data2 = list()
data3 = list()
data4 = list()
for i in range(25, 1000):
    s1aa = scenar1aa.solutions[i]
    s1ab = scenar1ab.solutions[i]
    s1ac = scenar1ac.solutions[i]
    base = baseline.solutions[i]
    data1.append(base['CARb1'])
    data2.append(s1aa['CARb1'])
    data3.append(s1ab['CARb1'])
    data4.append(s1ac['CARb1'])
    
fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='-', color='k', label='Baseline')
g2, = axes.plot(data2, linestyle='--', color='k', label='+10% shock')
g3, = axes.plot(data3, linestyle='-.', color='k', label='+30% shock')
g4, = axes.plot(data4, linestyle=':', color='k', label='+50% shock')

plt.legend(handles=[g1,g2,g3,g4], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%
    
caption = '''
    Figure 2 : State of the contigent convertible trigger following an increase in defaulted loans 
    (1 = not activated ; 0 = activated) '''

data1 = list()
data2 = list()
data3 = list()
data4 = list()
for i in range(20, 1000):
    s1aa = scenar1aa.solutions[i]
    s1ab = scenar1ab.solutions[i]
    s1ac = scenar1ac.solutions[i]    
    base = baseline.solutions[i]
    data1.append(base['indicKRb1'])
    data2.append(s1aa['indicKRb1'])
    data3.append(s1ab['indicKRb1'])
    data4.append(s1ac['indicKRb1'])
   
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='-', color='k', label='Baseline')
g2, = axes.plot(data2, linestyle='--', color='k', label='+10% shock')
g3, = axes.plot(data3, linestyle='-.', color='k', label='+30% shock')
g4, = axes.plot(data4, linestyle=':', color='k', label='+50% shock')

plt.legend(handles=[g1,g2,g3,g4], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);


#%%
    
caption = '''
    Figure 3 : Evolution of the net value of investing households, relative to the scenario 
    without any activation of coco bonds, following an increase in the share of defaulted loans'''

data1 = list()
data2 = list()
data3 = list()
for i in range(20, 1000):
    s1aa = scenar1aa.solutions[i]
    s1ba = scenar1ba.solutions[i]
    s1ab = scenar1ab.solutions[i]
    s1bb = scenar1bb.solutions[i]
    s1ac = scenar1ac.solutions[i]
    s1bc = scenar1bc.solutions[i]
    data1.append(s1aa['V_r'] / s1ba['V_r'])
    data2.append(s1ab['V_r'] / s1bb['V_r'])
    data3.append(s1ac['V_r'] / s1bc['V_r'])
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g2, = axes.plot(data1, linestyle='--', color='k', label='+10% shock')
g3, = axes.plot(data2, linestyle='-.', color='k', label='+30% shock')
g4, = axes.plot(data3, linestyle=':', color='k', label='+50% shock')

plt.legend(handles=[g2,g3,g4], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.12, caption, csfont);

#%%
    
caption = '''
    Figure 4 : Evolution of the disposable income of investing households, relative to 
    the scenario without any activation of coco bonds, following an increase in the share
    of defaulted loans'''

data1 = list()
data2 = list()
data3 = list()
for i in range(20, 1000):
    s1aa = scenar1aa.solutions[i]
    s1ba = scenar1ba.solutions[i]
    s1ab = scenar1ab.solutions[i]
    s1bb = scenar1bb.solutions[i]
    s1ac = scenar1ac.solutions[i]
    s1bc = scenar1bc.solutions[i]
    data1.append(s1aa['YDHS_r'] / s1ba['YDHS_r'])
    data2.append(s1ab['YDHS_r'] / s1bb['YDHS_r'])
    data3.append(s1ac['YDHS_r'] / s1bc['YDHS_r'])
    
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g2, = axes.plot(data1, linestyle='--', color='k', label='+10% shock')
g3, = axes.plot(data2, linestyle='-.', color='k', label='+30% shock')
g4, = axes.plot(data3, linestyle=':', color='k', label='+50% shock')

plt.legend(handles=[g2,g3,g4], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.12, caption, csfont);

#%%
    
caption = '''
    Figure 5 : Evolution of the consumption of investing households, relative to the scenario without
    any activation of coco bonds, following an increase in the share of defaulted loans'''

data1 = list()
data2 = list()
data3 = list()
for i in range(20, 1000):
    s1aa = scenar1aa.solutions[i]
    s1ba = scenar1ba.solutions[i]
    s1ab = scenar1ab.solutions[i]
    s1bb = scenar1bb.solutions[i]
    s1ac = scenar1ac.solutions[i]
    s1bc = scenar1bc.solutions[i]
    data1.append(s1aa['C_r'] / s1ba['C_r'])
    data2.append(s1ab['C_r'] / s1bb['C_r'])
    data3.append(s1ac['C_r'] / s1bc['C_r'])
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g2, = axes.plot(data1, linestyle='--', color='k', label='+10% shock')
g3, = axes.plot(data2, linestyle='-.', color='k', label='+30% shock')
g4, = axes.plot(data3, linestyle=':', color='k', label='+50% shock')

plt.legend(handles=[g2,g3,g4], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%
    
caption = '''
    Figure 6 : Evolution of the net value of firms, relative to the scenario 
    without any activation of coco bonds, following an increase in the share of defaulted loans'''

data1 = list()
data2 = list()
data3 = list()
for i in range(20, 1000):
    s1aa = scenar1aa.solutions[i]
    s1ba = scenar1ba.solutions[i]
    s1ab = scenar1ab.solutions[i]
    s1bb = scenar1bb.solutions[i]
    s1ac = scenar1ac.solutions[i]
    s1bc = scenar1bc.solutions[i]
    data1.append(s1aa['V_f'] / s1ba['V_f'])
    data2.append(s1ab['V_f'] / s1bb['V_f'])
    data3.append(s1ac['V_f'] / s1bc['V_f'])
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g2, = axes.plot(data1, linestyle='--', color='k', label='+10% shock')
g3, = axes.plot(data2, linestyle='-.', color='k', label='+30% shock')
g4, = axes.plot(data3, linestyle=':', color='k', label='+50% shock')

plt.legend(handles=[g2,g3,g4], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.12, caption, csfont);


#%%
    
caption = '''
    Figure 7 : Evolution of firms' investment', relative to the scenario 
    without any activation of coco bonds, following an increase in the share of defaulted loans'''

data1 = list()
data2 = list()
data3 = list()
for i in range(20, 1000):
    s1aa = scenar1aa.solutions[i]
    s1ba = scenar1ba.solutions[i]
    s1ab = scenar1ab.solutions[i]
    s1bb = scenar1bb.solutions[i]
    s1ac = scenar1ac.solutions[i]
    s1bc = scenar1bc.solutions[i]
    data1.append(s1aa['INV'] / s1ba['INV'])
    data2.append(s1ab['INV'] / s1bb['INV'])
    data3.append(s1ac['INV'] / s1bc['INV'])
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g2, = axes.plot(data1, linestyle='--', color='k', label='+10% shock')
g3, = axes.plot(data2, linestyle='-.', color='k', label='+30% shock')
g4, = axes.plot(data3, linestyle=':', color='k', label='+50% shock')

plt.legend(handles=[g2,g3,g4], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.12, caption, csfont);

#%%

caption = '''
    Figure 8 : Evolution of the wage bill of working households following an increase in defaulted loans
    in both crisis scenario (with and without activation of coco bonds)'''

data1 = list()
data2 = list()
data3 = list()

for i in range(20, 1000):
    s1aa = scenar1aa.solutions[i]
    s1ba = scenar1ba.solutions[i]
    s1ab = scenar1ab.solutions[i]
    s1bb = scenar1bb.solutions[i]
    s1ac = scenar1ac.solutions[i]
    s1bc = scenar1bc.solutions[i]
    base = baseline.solutions[i]
    data1.append(s1aa['WB'] / s1ba['WB'])
    data2.append(s1ab['WB'] / s1bb['WB'])
    data3.append(s1ac['WB'] / s1bc['WB'])

    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g2, = axes.plot(data1, linestyle='--', color='k', label='+10% shock')
g3, = axes.plot(data2, linestyle='-.', color='k', label='+30% shock')
g4, = axes.plot(data3, linestyle=':', color='k', label='+50% shock')

plt.legend(handles=[g2,g3,g4], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%
    
caption = '''
    Figure 9 : Evolution of the consumption of working households, relative to the scenario without
    any activation of coco bonds, following an increase in the share of defaulted loans'''

data1 = list()
data2 = list()
data3 = list()
for i in range(20, 1000):
    s1aa = scenar1aa.solutions[i]
    s1ba = scenar1ba.solutions[i]
    s1ab = scenar1ab.solutions[i]
    s1bb = scenar1bb.solutions[i]
    s1ac = scenar1ac.solutions[i]
    s1bc = scenar1bc.solutions[i]
    data1.append(s1aa['C_w'] / s1ba['C_w'])
    data2.append(s1ab['C_w'] / s1bb['C_w'])
    data3.append(s1ac['C_w'] / s1bc['C_w'])
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g2, = axes.plot(data1, linestyle='--', color='k', label='+10% shock')
g3, = axes.plot(data2, linestyle='-.', color='k', label='+30% shock')
g4, = axes.plot(data3, linestyle=':', color='k', label='+50% shock')

plt.legend(handles=[g2,g3,g4], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont)


#%%
    
caption = '''
    Figure 10 : Evolution of the net value of retails banks following an increase in defaulted loans
    in both crisis scenario (with and without activation of coco bonds)'''

data1 = list()
data2 = list()
data3 = list()


for i in range(20, 1000):
    s1aa = scenar1aa.solutions[i]
    s1ba = scenar1ba.solutions[i]
    s1ab = scenar1ab.solutions[i]
    s1bb = scenar1bb.solutions[i]
    s1ac = scenar1ac.solutions[i]
    s1bc = scenar1bc.solutions[i]
    base = baseline.solutions[i]
    data1.append((100000000 + s1aa['V_b1']) / (100000000 + s1ba['V_b1']))
    data2.append((100000000 + s1ab['V_b1']) / (100000000 + s1bb['V_b1']))
    data3.append((100000000 + s1ac['V_b1']) / (100000000 + s1bc['V_b1']))
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g2, = axes.plot(data1, linestyle='--', color='k', label='+10% shock')
g3, = axes.plot(data2, linestyle='-.', color='k', label='+30% shock')
g4, = axes.plot(data3, linestyle=':', color='k', label='+50% shock')

plt.legend(handles=[g2,g3,g4], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);


#%%

#INDICATEURS D'INSTABILITÉ

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

for i in range(20, 50):
    s1ab = scenar1ab.solutions[i]
    s1bb = scenar1bb.solutions[i]
    base = baseline.solutions[i]
    data1.append(s1ab['Ygrowth'])
    data2.append(s1bb['Ygrowth'])
    data3.append(s1ab['Cgrowth'])
    data4.append(s1bb['Cgrowth'])
    data5.append(s1ab['V_rgrowth'])
    data6.append(s1bb['V_rgrowth'])
    data7.append(s1ab['V_wgrowth'])
    data8.append(s1bb['V_wgrowth'])
    data9.append(s1ab['V_fgrowth'])
    data10.append(s1bb['V_fgrowth'])
    data11.append(s1ab['V_b1growth'])
    data12.append(s1bb['V_b1growth'])


#%%
import numpy as np

print((np.std(data1))/(np.std(data2)))
print((np.std(data3))/(np.std(data4)))
print((np.std(data5))/(np.std(data6)))
print((np.std(data7))/(np.std(data8)))
print((np.std(data9))/(np.std(data10)))
print((np.std(data11))/(np.std(data12)))

#%%
        
#SCENARIO 2Aa : dépréciation du prix des actions d'entreprises avec activation de coco bonds

scenar2aa = create_kremer_model()
scenar2aa.set_values(parameters)
scenar2aa.set_values(exogenous)
scenar2aa.set_values(variables)


for _ in range(40):
    scenar2aa.solve(iterations=2000, threshold=1e-6)
    
scenar2aa.set_values({'KRT2': 0.025})
scenar2aa.set_values({'lambda40': 0.1})


for _ in range(1960):
    scenar2aa.solve(iterations=2000, threshold=1e-6)
    


#SCENARIO 2Ba : dépréciation du prix des actions d'entreprises sans activation de coco bonds

scenar2ba = create_kremer_model()
scenar2ba.set_values(parameters)
scenar2ba.set_values(exogenous)
scenar2ba.set_values(variables)

scenar2ba.set_values({'KRT2': 100000})

for _ in range(40):
    scenar2ba.solve(iterations=2000, threshold=1e-6)

scenar2ba.set_values({'lambda40': 0.1})


for _ in range(1960):
    scenar2ba.solve(iterations=2000, threshold=1e-6)
    
    

#%%
        
#SCENARIO 2Ab : dépréciation du prix des actions d'entreprises avec activation de coco bonds

scenar2ab = create_kremer_model()
scenar2ab.set_values(parameters)
scenar2ab.set_values(exogenous)
scenar2ab.set_values(variables)



for _ in range(40):
    scenar2ab.solve(iterations=2000, threshold=1e-6)
    
scenar2ab.set_values({'KRT2': 0.025})
scenar2ab.set_values({'lambda40': 0.2})



for _ in range(1960):
    scenar2ab.solve(iterations=2000, threshold=1e-6)
    


#SCENARIO 2Bb : dépréciation du prix des actions d'entreprises sans activation de coco bonds

scenar2bb = create_kremer_model()
scenar2bb.set_values(parameters)
scenar2bb.set_values(exogenous)
scenar2bb.set_values(variables)

scenar2bb.set_values({'KRT2': 100000})

for _ in range(40):
    scenar2bb.solve(iterations=2000, threshold=1e-6)

scenar2bb.set_values({'lambda40': 0.2})


for _ in range(1960):
    scenar2bb.solve(iterations=2000, threshold=1e-6)
    
    
#%%
    
caption = '''
    Figure 11 : Standard deviation of firm equity prices following a decrease in preferences for them
    '''

data1 = list()
data2 = list()
data3 = list()
data4 = list()

for i in range(30, 200):
    base = baseline.solutions[i]
    s2aa = scenar2aa.solutions[i]
    s2ab = scenar2ab.solutions[i]
    data1.append(base['pestd'])
    data2.append(s2aa['pestd'])
    data3.append(s2ab['pestd'])

fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='-', color='k', label='baseline')
g2, = axes.plot(data2, linestyle=':', color='k', label='-60% shock')
g3, = axes.plot(data3, linestyle='-.', color='k', label='-20% shock')

plt.legend(handles=[g1,g2,g3], prop={'family': 'Times New Roman', 'size':12})


fig.text(0.1, -.09, caption, csfont);



#%%
    
caption = '''
    Figure 12 : State of the contigent convertible trigger following a decrease in preferences for
    firm equities (1 = not activated ; 0 = activated) 
    '''

data1 = list()
data2 = list()
data3 = list()
data4 = list()

for i in range(30, 200):
    base = baseline.solutions[i]
    s2aa = scenar2aa.solutions[i]
    s2ab = scenar2ab.solutions[i]
    data1.append(base['indicKRb2'])
    data2.append(s2aa['indicKRb2'])
    data3.append(s2ab['indicKRb2'])

fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='-', color='k', label='baseline')
g2, = axes.plot(data2, linestyle=':', color='k', label='-60% shock')
g3, = axes.plot(data3, linestyle='-.', color='k', label='-20% shock')

plt.legend(handles=[g1,g2,g3], prop={'family': 'Times New Roman', 'size':12})


fig.text(0.1, -.09, caption, csfont);


#%%
    
caption = '''
    Figure 13 : Evolution of the net values of investing households, relative to the scenario 
    without any activation of coco bonds, following a decrease in preferences for firm equities 
    '''

data1 = list()
data2 = list()
data3 = list()
for i in range(0,1000):
    s2aa = scenar2aa.solutions[i]
    s2ba = scenar2ba.solutions[i]
    s2ab = scenar2ab.solutions[i]
    s2bb = scenar2bb.solutions[i] 
    data1.append(s2aa['V_r'] / s2ba['V_r'])
    data2.append(s2ab['V_r'] / s2bb['V_r'])
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='-.', color='k', label='-60% shock')
g2, = axes.plot(data2, linestyle=':', color='k', label='-20% shock')

plt.legend(handles=[g1,g2], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%
    
caption = '''
    Figure 14 : Evolution of the disposable income of investing households, relative to the scenario 
    without any activation of coco bonds, following a decrease in preferences for firm equities 
    '''

data1 = list()
data2 = list()
data3 = list()
for i in range(0,1000):
    s2aa = scenar2aa.solutions[i]
    s2ba = scenar2ba.solutions[i]
    s2ab = scenar2ab.solutions[i]
    s2bb = scenar2bb.solutions[i]
    data1.append(s2aa['YD_r'] / s2ba['YD_r'])
    data2.append(s2ab['YD_r'] / s2bb['YD_r'])
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='-.', color='k', label='-60% shock')
g2, = axes.plot(data2, linestyle=':', color='k', label='-20% shock')

plt.legend(handles=[g1,g2], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%

caption = '''
    Figure 15 : Evolution of the consumption of investing households, relative to the scenario 
    without any activation of coco bonds, following a decrease in preferences for firm equities 
    '''
    
data1 = list()
data2 = list()
data3 = list()
for i in range(0,1000):
    s2aa = scenar2aa.solutions[i]
    s2ba = scenar2ba.solutions[i]
    s2ab = scenar2ab.solutions[i]
    s2bb = scenar2bb.solutions[i]
    data1.append(s2aa['C_r'] / s2ba['C_r'])
    data2.append(s2ab['C_r'] / s2bb['C_r'])
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='-.', color='k', label='-60% shock')
g2, = axes.plot(data2, linestyle=':', color='k', label='-20% shock')

plt.legend(handles=[g1,g2], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption, csfont);

#%%
    
caption = '''
    Figure 16 : Evolution of the net value of firms, relative to the scenario 
    without any activation of coco bonds, following a decrease in preferences for firm equities 
    '''

data1 = list()
data2 = list()
data3 = list()
for i in range(0,2000):
    s2aa = scenar2aa.solutions[i]
    s2ba = scenar2ba.solutions[i]
    s2ab = scenar2ab.solutions[i]
    s2bb = scenar2bb.solutions[i]
    data1.append(s2aa['V_f'] / s2ba['V_f'])
    data2.append(s2ab['V_f'] / s2bb['V_f'])
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='-.', color='k', label='-60% shock')
g2, = axes.plot(data2, linestyle=':', color='k', label='-20% shock')

plt.legend(handles=[g1,g2], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption);

#%%
    
caption = '''
    Figure 17 : Evolution of the investment of firms, relative to the scenario 
    without any activation of coco bonds, following a decrease in preferences for firm equities 
    '''

data1 = list()
data2 = list()
data3 = list()
for i in range(0,1000):
    s2aa = scenar2aa.solutions[i]
    s2ba = scenar2ba.solutions[i]
    s2ab = scenar2ab.solutions[i]
    s2bb = scenar2bb.solutions[i]
    data1.append(s2aa['INV'] / s2ba['INV'])
    data2.append(s2ab['INV'] / s2bb['INV'])
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='-.', color='k', label='-60% shock')
g2, = axes.plot(data2, linestyle=':', color='k', label='-20% shock')

plt.legend(handles=[g1,g2], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption);

#%%
    
caption = '''
    Figure 18 : Evolution of the wage bill of working households, relative to the scenario 
    without any activation of coco bonds, following a decrease in preferences for firm equities 
    '''

data1 = list()
data2 = list()
data3 = list()
for i in range(0,1000):
    s2aa = scenar2aa.solutions[i]
    s2ba = scenar2ba.solutions[i]
    s2ab = scenar2ab.solutions[i]
    s2bb = scenar2bb.solutions[i]
    data1.append(s2aa['WB'] / s2ba['WB'])
    data2.append(s2ab['WB'] / s2bb['WB'])
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='-.', color='k', label='-60% shock')
g2, = axes.plot(data2, linestyle=':', color='k', label='-20% shock')

plt.legend(handles=[g1,g2], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption);

#%%
    
caption = '''
    Figure 19 : Evolution of the consumption of working households, relative to the scenario 
    without any activation of coco bonds, following a decrease in preferences for firm equities 
    '''

data1 = list()
data2 = list()
data3 = list()
for i in range(0,1000):
    s2aa = scenar2aa.solutions[i]
    s2ba = scenar2ba.solutions[i]
    s2ab = scenar2ab.solutions[i]
    s2bb = scenar2bb.solutions[i]
    data1.append(s2aa['c_w'] / s2ba['c_w'])
    data2.append(s2ab['c_w'] / s2bb['c_w'])
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='-.', color='k', label='-60% shock')
g2, = axes.plot(data2, linestyle=':', color='k', label='-20% shock')

plt.legend(handles=[g1,g2], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption);




#%%
    
caption = '''
    Figure 20 : Evolution of the net value of investment banks, relative to the scenario 
    without any activation of coco bonds, following a decrease in preferences for firm equities 
    '''

data1 = list()
data2 = list()
data3 = list()
for i in range(0,1000):
    s2aa = scenar2aa.solutions[i]
    s2ba = scenar2ba.solutions[i]
    s2ab = scenar2ab.solutions[i]
    s2bb = scenar2bb.solutions[i]
    data1.append(s2aa['V_b2'] / s2ba['V_b2'])
    data2.append(s2ab['V_b2'] / s2bb['V_b2'])
    
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 1.1, 1.1])
axes.tick_params(top='off', right='off')
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
#axes.set_ylim(-1, 2)

csfont = {'fontname':'Times New Roman', 'size':'12'}

g1, = axes.plot(data1, linestyle='-.', color='k', label='-60% shock')
g2, = axes.plot(data2, linestyle=':', color='k', label='-20% shock')

plt.legend(handles=[g1,g2], prop={'family': 'Times New Roman', 'size':12})

fig.text(0.1, -.09, caption);



#%%

#INDICATEURS D'INSTABILITÉ

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

for i in range(5, 50):
    s2aa = scenar2aa.solutions[i]
    s2ba = scenar2ba.solutions[i]
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
