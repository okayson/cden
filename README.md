# cden

## Requirements

* cdの効率化
	* 移動履歴を表示->選択して移動可能とする
	* `.`を入力したら、カレントディレクトリ以下を表示->選択して移動可能とする

* 移動履歴の管理
	* cdの都度、移動先+移動回数を記録する
	* 記録数には最大数を設ける
	* 記録数の上限に達した場合は移動回数の少ないものから削除する
	* homeへの移動、..での移動(?)、カレントディレクトリへの移動は管理対象としない

* 移動履歴の表示
	* 先頭にはhomeを表示する(cd + enterでhomeに移動できるように)
	* 現在のパスを含むパスを先頭に表示する
	* 現在の下位ディレクトリを表示する（時間がかかるかも、./と入力したら、とかのほうが良いかも) 

## Implementaton notes

* 絶対パスで記録する
* symbolic linkはそのまま記録する

## Name candidate
* acceleratedcd
* accelcd
* accd

## Note
```shell
function ac(){
	# $1 : empty	=> 履歴から候補を表示
	#	 : .		=> CurrentDirから候補を表示
	#	 : <dir>	=> 何もしない
	dir = accd.py $1
	if [ -n "$1" ]; then
		accd.py
	elif
		accd.py $1
	else
		cd $1
	fi
}
```

