import pandas as pd

# id,class,cap-diameter,cap-shape,cap-surface,cap-color,does-bruise-or-bleed,gill-attachment,gill-spacing,gill-color,stem-height,stem-width,stem-root,stem-surface,stem-color,veil-type,veil-color,has-ring,ring-type,spore-print-color,habitat,season
# class;cap-diameter;cap-shape;cap-surface;cap-color;does-bruise-or-bleed;gill-attachment;gill-spacing;gill-color;stem-height;stem-width;'stem-color;has-ring;ring-type;habitat;season
mushroom_df = pd.read_csv('files/data/data/secondary_data_no_miss.csv', delimiter=';', low_memory=False)

df_new = pd.DataFrame()

df_new['id'] = range(len(mushroom_df))

df_new['class'] = mushroom_df['class']
df_new['cap-diameter'] = mushroom_df['cap-diameter']
df_new['cap-shape'] = mushroom_df['cap-shape']
df_new['cap-surface'] = mushroom_df['cap-surface']
df_new['cap-color'] = mushroom_df['cap-color']
df_new['does-bruise-or-bleed'] = mushroom_df['does-bruise-or-bleed']
df_new['gill-attachment'] = mushroom_df['gill-attachment']
df_new['gill-spacing'] = mushroom_df['gill-spacing']
df_new['gill-color'] = mushroom_df['gill-color']
df_new['stem-height'] = mushroom_df['stem-height']
df_new['stem-width'] = mushroom_df['stem-width']
df_new['stem-root'] = mushroom_df['stem-root'] if 'stem-root' in mushroom_df.columns else ""
df_new['stem-surface'] = mushroom_df['stem-surface'] if 'stem-surface' in mushroom_df.columns else ""
df_new['stem-color'] = mushroom_df['stem-color']
df_new['veil-type'] = mushroom_df['veil-type'] if 'veil-type' in mushroom_df.columns else ""
df_new['veil-color'] = mushroom_df['veil-color'] if 'veil-color' in mushroom_df.columns else ""
df_new['has-ring'] = mushroom_df['has-ring']
df_new['ring-type'] = mushroom_df['ring-type']
df_new['spore-print-color'] = mushroom_df['spore-print-color'] if 'spore-print-color' in mushroom_df.columns else ""
df_new['habitat'] = mushroom_df['habitat']
df_new['season'] = mushroom_df['season']

print("DONE")
# 병합된 결과를 새로운 CSV 파일로 저장
df_new.to_csv('modified_data/secondary_data_no_miss_modify.csv', index=False)