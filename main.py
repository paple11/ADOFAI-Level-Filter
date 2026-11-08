# sample/2021 (기본 테스트)/main.adofai
# sample/230 (최적화 테스트)/230.adofai

"""
`SetSpeed`, `Twirl`, `SetHitsound`, `SetPlanetRotation`, `Pause`
`SetPlanetSize`, `MoveTrack`, `PositionTrack`, `MoveCamera`, `Hold`, `MultiPlanet`,
`FreeRoam`, `ScaleMargin`, `ScaleRadius`, `PlaySound`, `AnimateTrack`, `RepeatEvents`
`Checkpoint`, `KillPlayer`, `AutoPlayTiles`, `Multitap`, `FreeRoamTwirl`, `FreeRoamRemove`
`TileDimensions`, `Hide`, `SetInputEvent`
"""


from pathlib import Path
import os
import json5
import time
import subprocess
import json
import shutil

except_names = ['backup.adofai']
music_extension = ('.mp3', '.ogg', '.wav', '.flac')


def ct() :
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

def read_level(path):
    print(f'Reading "{Path(path).name}"...')

    with open(path, 'r', encoding='utf-8-sig') as f:
        content = f.read()

    try:
        print('Parsing with JSON...')
        data = json.loads(content)
        
    except json.JSONDecodeError: # 마지막 요소에 쉼표 넣는 이상한 사람들 때문에 추가합니다..
        print('Parsing with JSON5...')
        data = json5.loads(content)

    return data


def save_level(data, level_path):
    level_path = Path(level_path)

    output_dir = level_path.parent / 'Filtered'
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / f'{level_path.stem}_filtered.adofai'

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))

    for file in level_path.parent.iterdir():
        if file.is_file() and file.name.lower().endswith(music_extension):
            shutil.copy2(file, output_dir / file.name)

    print(f'Saved: "{output_path}"')


def choose_level(level_path) :
    parent_path = Path(level_path).name
    adofai_files = [f for f in os.listdir(level_path)
                    if f.endswith('.adofai')
                    and f not in except_names
                    and os.path.isfile(os.path.join(level_path, f))]
    if len(adofai_files) == 0 : return None
    if len(adofai_files) == 1 : return str(Path(level_path) / adofai_files[0])
    while True :
        print('=' * 20)
        for i, file in enumerate(adofai_files, start=1) :
            print(f'{i}. {parent_path}\\{file}')
        print('=' * 20)
        num = input('필터링할 레벨을 선택하세요(번호로 입력): ')
        if num.isdigit() and 1 <= int(num) <= len(adofai_files) :
            num = int(num)
            break
        print('잘못된 입력입니다.')
        time.sleep(3)
        ct()
    return str(Path(level_path) / adofai_files[num - 1])


def filter(data) :
    keep_events = [
        'SetSpeed', 'Twirl', 'SetHitsound', 'SetPlanetRotation', 'Pause',
        'SetPlanetSize', 'MoveTrack', 'PositionTrack', 'MoveCamera', 'Hold',
        'MultiPlanet', 'FreeRoam', 'ScaleMargin', 'ScaleRadius', 'PlaySound',
        'AnimateTrack', 'RepeatEvents', 'Checkpoint', 'KillPlayer',
        'AutoPlayTiles', 'Multitap', 'FreeRoamTwirl', 'FreeRoamRemove',
        'TileDimensions', 'Hide', 'SetInputEvent'
    ]
    filtered_actions = []


    for action in data['actions']:
        if action['eventType'] not in keep_events:
            print(
                f"\r\033[2KRemoved: {action['eventType']} (Floor: {action.get('floor', '?')})",
                end='', flush=True
            )
            continue

        filtered_actions.append(action)
    print()
    data['actions'] = filtered_actions
    data['settings']['trackStyle'] = 'Standard'
    data['settings']['trackColor'] = 'debb7bff'
    data['settings']['backgroundColor'] = '000000'
    data['settings']['trackColorType'] = 'Single'
    data['decorations'] = []



if __name__ == "__main__" :
    ct()
    level_path = input('레벨 파일이 있는 폴더 경로를 입력하세요: ')
    level = choose_level(level_path)
    if level :
        data = read_level(level)
        filter(data)
        save_level(data, level)
    else :
        print('해당 경로에서 레벨 파일을 찾지 못했습니다.')
