from twitter_operator import TwitterOperator

tweet_content = "これだけは言わせてください。\n\n「未経験からWEBエンジニア転職」に高額な教材等は必要ありません!!\n\nこちらの記事で私自身が転職活動中に得た転職の戦略を紹介していますので、本気で転職をしたいという方だけぜひ読んでみてください。\n\n#駆け出しエンジニアと繋がりたい\nhttps://note.com/maasaayaan1126/n/ndd2cd29f899c"

twitter_operator = TwitterOperator()
result = twitter_operator.tweet(tweet_content)
