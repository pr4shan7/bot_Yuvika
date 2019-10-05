from init import api, follow_list, following_list


def follow_op():
    for i in follow_list:
        if (i not in following_list):
            follower = api.get_user(i)
            follower.follow()


def unfollow_op():
    for i in following_list:
        if (i not in follow_list):
            unfollower = api.get_user(i)
            unfollower.unfollow()
