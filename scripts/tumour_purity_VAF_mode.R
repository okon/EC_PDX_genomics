estimate_mode <- function(x) {
  d <- density(x)
  d$x[which.max(d$y)]
}


df_maf_sp %>%
  left_join(df_clin) %>%
  filter(PDX %in% c("PDX12","PDX52","PDX58","PDX59")) %>%
  mutate(VAF = as.numeric(T_Alt_Count)/(as.numeric(T_Ref_Count)+as.numeric(T_Alt_Count))*100) %>%
  group_by(PDX,SampleLabel) %>%
  summarise(mode = estimate_mode(VAF)*2) #x2 because tumour purity is 2 and most som. mutations are heterozygous
