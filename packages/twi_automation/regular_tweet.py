import datetime
from twitter_operator import TwitterOperator

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)

tweet_content = "これだけは言わせてください\n\n未経験からWEBエンジニア転職に高額な教材等は不要です\n\n私自身が転職活動で得た戦略を紹介していますので、本気で転職をしたいという方だけ読んでみてください。\n\n#駆け出しエンジニアと繋がりたい\n\nhttps://note.com/maasaayaan1126/n/ndd2cd29f899c\n\n"f"{now.strftime('%Y年%m月%d日 %H:%M:%S')}"

twitter_operator = TwitterOperator()
twitter_operator.tweet(tweet_content)
