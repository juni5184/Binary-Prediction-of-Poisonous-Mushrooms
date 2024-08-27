import pandas as pd

# CSV 파일 불러오기
# id,class,cap-diameter,cap-shape,cap-surface,cap-color,does-bruise-or-bleed,gill-attachment,gill-spacing,gill-color,stem-height,stem-width,stem-root,stem-surface,stem-color,veil-type,veil-color,has-ring,ring-type,spore-print-color,habitat,season
# class;cap-diameter-min;cap-diameter-max;cap-shape;cap-surface;cap-color;does-bruis-or-bleed;gill-attachment;gill-spacing;gill-color;stem-height-min;stem-height-max;stem-width-min;stem-width-max;stem-root;stem-surface;stem-color;veil-type;veil-color;has-ring;ring-type;spore-color;habitat;season
mushroom_df = pd.read_csv('files/data/data/secondary_data_generated_with_intervals.csv', delimiter=';', low_memory=False)

# 새로운 목표 컬럼 구조 생성
df_new = pd.DataFrame()

# id 컬럼 추가
df_new['id'] = range(len(mushroom_df))

# class 컬럼 복사
df_new['class'] = mushroom_df['class']

df_new['cap-diameter'] = mushroom_df[['cap-diameter-min', 'cap-diameter-max']].mean(axis=1)

df_new['cap-shape'] = mushroom_df['cap-shape']
df_new['cap-surface'] = mushroom_df['cap-surface']
df_new['cap-color'] = mushroom_df['cap-color']
df_new['does-bruise-or-bleed'] = mushroom_df['does-bruis-or-bleed']
df_new['gill-attachment'] = mushroom_df['gill-attachment']
df_new['gill-spacing'] = mushroom_df['gill-spacing']
df_new['gill-color'] = mushroom_df['gill-color']

df_new['stem-height'] = mushroom_df[['stem-height-min', 'stem-height-max']].mean(axis=1)
df_new['stem-width'] = mushroom_df[['stem-width-min', 'stem-width-max']].mean(axis=1)
df_new['stem-root'] = mushroom_df['stem-root']
df_new['stem-surface'] = mushroom_df['stem-surface']
df_new['stem-color'] = mushroom_df['stem-color']

df_new['veil-type'] = mushroom_df['veil-type']
df_new['veil-color'] = mushroom_df['veil-color']
df_new['has-ring'] = mushroom_df['has-ring']
df_new['ring-type'] = mushroom_df['ring-type']
df_new['spore-print-color'] = mushroom_df['spore-color']
df_new['habitat'] = mushroom_df['habitat']
df_new['season'] = mushroom_df['season'] if 'season' in mushroom_df.columns else ""

# 병합된 결과를 새로운 CSV 파일로 저장
df_new.to_csv('modified_data/secondary_data_generated_with_intervals_modify.csv', index=False)