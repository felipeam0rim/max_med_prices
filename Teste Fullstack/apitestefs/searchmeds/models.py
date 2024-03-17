from django.db import models

class MedProfile(models.Model):
    profile_id = models.BigIntegerField(primary_key=True)
    substancia = models.CharField(max_length=10000, null=True)
    cnpj = models.CharField(max_length=18, null=True)
    laboratorio = models.CharField(max_length=10000, null=True)
    codigo_ggrem = models.CharField(max_length=20, null=True)
    registro = models.CharField(max_length=20, null=True)
    ean_1 = models.CharField(max_length=20, null=True)
    ean_2 = models.CharField(max_length=20, null=True)
    ean_3 = models.CharField(max_length=20, null=True)
    produto = models.CharField(max_length=10000, null=True)
    apresentacao = models.CharField(max_length=10000, null=True)
    classe_terapeutica = models.CharField(max_length=10000, null=True)
    tipo_de_produto = models.CharField(max_length=10000, null=True)
    regime_de_preco = models.CharField(max_length=10000, null=True)
    pf_sem_imposto = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    pf_0 = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    pf_12 = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    pf_12_alc = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    pf_17 = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    pf_17_alc = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    pf_17_5 = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    pf_17_5_alc = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    pf_18 = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    pf_18_alc = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    pf_19 = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    pf_19_alc = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    pf_19_5 = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    pf_19_5_alc = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    pf_20 = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    pf_20_alc = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    pf_20_5 = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    pf_21 = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    pf_21_alc = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    pf_22 = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    pf_22_alc = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    pmvg_sem_imposto = models.CharField(max_length=10, default="", null=True)
    pmvg_0 = models.CharField(max_length=10, default="", null=True)
    pmvg_12 = models.CharField(max_length=10, default="", null=True)
    pmvg_12_alc = models.CharField(max_length=10, default="", null=True)
    pmvg_17 = models.CharField(max_length=10, default="", null=True)
    pmvg_17_alc = models.CharField(max_length=10, default="", null=True)
    pmvg_17_5 = models.CharField(max_length=10, default="", null=True)
    pmvg_17_5_alc = models.CharField(max_length=10, default="", null=True)
    pmvg_18 = models.CharField(max_length=10, default="", null=True)
    pmvg_18_alc = models.CharField(max_length=10, default="", null=True)
    pmvg_19 = models.CharField(max_length=10, default="", null=True)
    pmvg_19_alc = models.CharField(max_length=10, default="", null=True)
    pmvg_19_5 = models.CharField(max_length=10, default="", null=True)
    pmvg_19_5_alc = models.CharField(max_length=10, default="", null=True)
    pmvg_20 = models.CharField(max_length=10, default="", null=True)
    pmvg_20_alc = models.CharField(max_length=10, default="", null=True)
    pmvg_20_5 = models.CharField(max_length=10, default="", null=True)
    pmvg_21 = models.CharField(max_length=10, default="", null=True)
    pmvg_21_alc = models.CharField(max_length=10, default="", null=True)
    pmvg_22 = models.CharField(max_length=10, default="", null=True)
    pmvg_22_alc = models.CharField(max_length=10, default="", null=True)
    restricao_hospitalar = models.CharField(max_length=50, default="", null=True)
    cap = models.CharField(max_length=50, default="", null=True)
    confaz_87 = models.CharField(max_length=50, default="", null=True)
    icms_0 = models.CharField(max_length=50, default="", null=True)
    analise_recursal = models.CharField(max_length=50, null=True)
    lista_conc_cred_trib = models.CharField(max_length=50, default="")
    comercializacao_2022 = models.CharField(max_length=50, default="")
    tarja = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.title
