import pandas as pd

# CSV 파일 불러오기
# id,class,cap-diameter,cap-shape,cap-surface,cap-color,does-bruise-or-bleed,gill-attachment,gill-spacing,gill-color,stem-height,stem-width,stem-root,stem-surface,stem-color,veil-type,veil-color,has-ring,ring-type,spore-print-color,habitat,season
# class;cap-shape;cap-surface;cap-color;bruises;odor;gill-attachment;gill-spacing;gill-size;gill-color;stalk-shape;stalk-root;stalk-surface-above-ring;stalk-surface-below-ring;stalk-color-above-ring;stalk-color-below-ring;veil-type;veil-color;ring-number;ring-type;spore-print-color;population;habitat
mushroom_df = pd.read_csv('files/data/data/1987_data_no_miss.csv', delimiter=';')

# 새로운 목표 컬럼 구조 생성
df_new = pd.DataFrame()

# id 컬럼 추가
df_new['id'] = range(len(mushroom_df))

# class 컬럼 복사
df_new['class'] = mushroom_df['class']

# 새로운 cap-diameter 컬럼 추가 (train.csv에서 데이터 가져옴)
df_new['cap-diameter'] = ""

# 1:1 매칭되는 컬럼 복사
df_new['cap-shape'] = mushroom_df['cap-shape']
df_new['cap-surface'] = mushroom_df['cap-surface']
df_new['cap-color'] = mushroom_df['cap-color']
df_new['does-bruise-or-bleed'] = mushroom_df['bruises']
df_new['gill-attachment'] = mushroom_df['gill-attachment']
df_new['gill-spacing'] = mushroom_df['gill-spacing']
df_new['gill-color'] = mushroom_df['gill-color']

# 나머지 새로 추가된 컬럼 (stem-height, stem-width, has-ring, season)도 빈 값으로 추가
df_new['stem-height'] = ""
df_new['stem-width'] = ""

df_new['stem-root'] = mushroom_df['stalk-root']

df_new['stem-surface'] = mushroom_df['stalk-surface-above-ring'].fillna('')# + mushroom_df['stalk-surface-below-ring'].fillna('')
df_new['stem-color'] = mushroom_df['stalk-color-above-ring'].fillna('')# + mushroom_df['stalk-color-below-ring'].fillna('')

df_new['veil-type'] = mushroom_df['veil-type']
df_new['veil-color'] = mushroom_df['veil-color']
df_new['has-ring'] = mushroom_df['ring-number'].apply(lambda x: 't' if x != 'n' else 'f')  # ring-number가 n이 아니면 t로 설정
df_new['ring-type'] = mushroom_df['ring-type']
df_new['spore-print-color'] = mushroom_df['spore-print-color']
df_new['habitat'] = mushroom_df['habitat']
df_new['season'] = ""

# 병합된 결과를 새로운 CSV 파일로 저장
df_new.to_csv('modified_data/1987_data_no_miss_modify.csv', index=False)

# 결과 확인
print(df_new.head())
