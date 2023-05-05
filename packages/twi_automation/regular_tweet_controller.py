from packages.twi_automation.Application.regular_tweet_use_case import RegularTweetUseCase
from shared.Domain.common.randomizer import Randomizer
from packages.twi_automation.Domain.regular_tweet_media_type import RegularTweetMediaType

random_media_types = [
    RegularTweetMediaType.NOTE,
    RegularTweetMediaType.YOUTUBE,
    # RegularTweetMediaType.TECH_BLOG
]
random_media_type_index: int = Randomizer().gen_random_int(0, len(random_media_types) - 1) #0～1
media_type_this_time = random_media_types[random_media_type_index]

RegularTweetUseCase().do_regular_tweet(media_type_this_time)
