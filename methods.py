from init import api, p7, p7_id, tweepy, follow_list, following_list


def follow_op():
    for i in follow_list:
        if (i not in following_list):
            # api.create_friendship(i)
            # api.create_friendship(i, 'follow')
            follower = api.get_user(i)
            follower.follow()


def unfollow_op():
    for i in following_list:
        if (i not in follow_list):
            # api.destroy_friendship(i)
            unfollower = api.get_user(i)
            unfollower.unfollow()
