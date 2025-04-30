set -e

mkdir -p csvs/sweep

for G in 25 50; do
  AREA=$((G*G))
  for M in 1 2 4; do
    MS=$((M*AREA))
    OUT=csvs/sweep/gs${G}x${G}_ms${MS}_r0.csv

    # Skip if we already have it
    if [ -f "$OUT" ]; then
      echo "Skipping existing $OUT"
      continue
    fi

    echo "Generating obs_radius=0 for ${G}×${G}, max_steps=${MS}"
    python -m experiments.partial_obs_q_train \
      --grid_size $G $G \
      --max_steps $MS \
      --obs_radius 0 \
      --episodes 2000 \
      --output $OUT
  done
done