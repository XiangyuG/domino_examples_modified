th = 100
NUM_ENTRIES = 4096

sketch_cnt_1 = [0] * NUM_ENTRIES;
sketch_cnt_2 = [0] * NUM_ENTRIES;
sketch_cnt_3 = [0] * NUM_ENTRIES;

def func(p):
  # Hash into count-min sketch location
  p.sketch1_idx = hash2a(p.sport, p.dport) % NUM_ENTRIES;
  p.sketch2_idx = hash2b(p.sport, p.dport) % NUM_ENTRIES;
  p.sketch3_idx = hash2c(p.sport, p.dport) % NUM_ENTRIES;

  # Detect heavy hitters
  if (sketch_cnt_1[p.sketch1_idx] > th and \
      sketch_cnt_2[p.sketch2_idx] > th and \
      sketch_cnt_3[p.sketch3_idx] > th) :
    p.heavy_hitter = 1;
  else:
    p.heavy_hitter = 0;

  # Increment count-min sketch locations
  sketch_cnt_1[p.sketch1_idx] += 1
  sketch_cnt_2[p.sketch2_idx] += 1
  sketch_cnt_3[p.sketch3_idx] += 1
