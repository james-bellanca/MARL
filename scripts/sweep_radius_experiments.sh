set -e

# Ensure output directory exists
mkdir -p csvs/sweep

# Configuration
GRID_SIZES=(25 50)
BUDDER_MULTS=(1 2 4)   # multiply area by 1, 2, and 4
RADII=("" 1 2)

for G in "${GRID_SIZES[@]}"; do
  AREA=$((G * G))
  for M in "${BUDDER_MULTS[@]}"; do
    MS=$((M * AREA))
    for R in "${RADII[@]}"; do
      TAG=${R:-full}
      OUT=csvs/sweep/gs${G}x${G}_ms${MS}_r${TAG}.csv
      echo "Running ${G}×${G}, max_steps=${MS}, obs_radius=${R:-None} → ${OUT}"
      python -m experiments.partial_obs_q_train \
        --grid_size $G $G \
        --max_steps $MS \
        ${R:+--obs_radius $R} \
        --episodes 2000 \
        --output $OUT
    done
  done
done