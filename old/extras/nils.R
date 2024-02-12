out = list()
for(i in 1:99) {
  for(j in 1:99) {
    for(k in 1:99) {
      if ((i + j + k) ^ 3 == as.integer(paste0(i, j, k))) {
        out = c(out, list(c(i, j, k)))
      }
    }
  }
}