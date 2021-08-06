"""
Generated by generator/generator.py - 2021-08-03 20:16:46.206915
"""
from pycasatunes.objects.media import CasaTunesMedia
from tests.responses.media_fixture import media_fixture_response


def test_media(media_fixture_response):
    obj = CasaTunesMedia(media_fixture_response)
    assert obj.SourceID == media_fixture_response["SourceID"]
    assert obj.QueueCount == media_fixture_response["QueueCount"]
    assert obj.QueueSongIndex == media_fixture_response["QueueSongIndex"]
    assert obj.ChangeQueueID == media_fixture_response["ChangeQueueID"]
    assert obj.ChangeMetaDataID == media_fixture_response["ChangeMetaDataID"]
    assert obj.ChangeBookmarkID == media_fixture_response["ChangeBookmarkID"]
    assert obj.BookmarkScope.ID == media_fixture_response["BookmarkScope"]["ID"]
    assert (
        obj.BookmarkScope.PersistentID
        == media_fixture_response["BookmarkScope"]["PersistentID"]
    )
    assert obj.BookmarkScope.Title == media_fixture_response["BookmarkScope"]["Title"]
    assert obj.BookmarkScope.Flags == media_fixture_response["BookmarkScope"]["Flags"]
    assert obj.Status == media_fixture_response["Status"]
    assert obj.Controls == media_fixture_response["Controls"]
    assert obj.RepeatMode == media_fixture_response["RepeatMode"]
    assert obj.ShuffleMode == media_fixture_response["ShuffleMode"]
    assert obj.CurrSong.Flags == media_fixture_response["CurrSong"]["Flags"]
    assert obj.CurrSong.QueueType == media_fixture_response["CurrSong"]["QueueType"]
    assert obj.CurrSong.ID == media_fixture_response["CurrSong"]["ID"]
    assert (
        obj.CurrSong.PersistentID == media_fixture_response["CurrSong"]["PersistentID"]
    )
    assert obj.CurrSong.Title == media_fixture_response["CurrSong"]["Title"]
    assert obj.CurrSong.Type == media_fixture_response["CurrSong"]["Type"]
    assert obj.CurrSong.ArtworkURI == media_fixture_response["CurrSong"]["ArtworkURI"]
    assert (
        obj.CurrSong.ArtworkRatio == media_fixture_response["CurrSong"]["ArtworkRatio"]
    )
    assert obj.CurrSong.Album == media_fixture_response["CurrSong"]["Album"]
    assert obj.CurrSong.Artists == media_fixture_response["CurrSong"]["Artists"]
    assert obj.CurrSong.Duration == media_fixture_response["CurrSong"]["Duration"]
    assert (
        obj.CurrSong.DeepLinks[0].Kind
        == media_fixture_response["CurrSong"]["DeepLinks"][0]["Kind"]
    )
    assert (
        obj.CurrSong.DeepLinks[0].Title
        == media_fixture_response["CurrSong"]["DeepLinks"][0]["Title"]
    )
    assert (
        obj.CurrSong.DeepLinks[0].Uri
        == media_fixture_response["CurrSong"]["DeepLinks"][0]["Uri"]
    )
    assert (
        obj.CurrSong.DeepLinks[0].MediaId
        == media_fixture_response["CurrSong"]["DeepLinks"][0]["MediaId"]
    )
    assert obj.CurrSong.BitRate == media_fixture_response["CurrSong"]["BitRate"]
    assert (
        obj.CurrSong.ListenerCount
        == media_fixture_response["CurrSong"]["ListenerCount"]
    )
    assert obj.CurrSong.Rating == media_fixture_response["CurrSong"]["Rating"]
    assert obj.CurrSong.TotalItems == media_fixture_response["CurrSong"]["TotalItems"]
    assert (
        obj.CurrSong.DisplayInfo[0]
        == media_fixture_response["CurrSong"]["DisplayInfo"][0]
    )
    assert (
        obj.CurrSong.ContextMenuItems[0].Type
        == media_fixture_response["CurrSong"]["ContextMenuItems"][0]["Type"]
    )
    assert (
        obj.CurrSong.ContextMenuItems[0].Key
        == media_fixture_response["CurrSong"]["ContextMenuItems"][0]["Key"]
    )
    assert (
        obj.CurrSong.ContextMenuItems[0].Title
        == media_fixture_response["CurrSong"]["ContextMenuItems"][0]["Title"]
    )
    assert (
        obj.CurrSong.ContextMenuItems[0].Value
        == media_fixture_response["CurrSong"]["ContextMenuItems"][0]["Value"]
    )
    assert obj.CurrSong.AccountName == media_fixture_response["CurrSong"]["AccountName"]
    assert obj.NextSong.Flags == media_fixture_response["NextSong"]["Flags"]
    assert obj.NextSong.QueueType == media_fixture_response["NextSong"]["QueueType"]
    assert obj.NextSong.ID == media_fixture_response["NextSong"]["ID"]
    assert (
        obj.NextSong.PersistentID == media_fixture_response["NextSong"]["PersistentID"]
    )
    assert obj.NextSong.Title == media_fixture_response["NextSong"]["Title"]
    assert obj.NextSong.Type == media_fixture_response["NextSong"]["Type"]
    assert obj.NextSong.ArtworkURI == media_fixture_response["NextSong"]["ArtworkURI"]
    assert (
        obj.NextSong.ArtworkRatio == media_fixture_response["NextSong"]["ArtworkRatio"]
    )
    assert obj.NextSong.Album == media_fixture_response["NextSong"]["Album"]
    assert obj.NextSong.Artists == media_fixture_response["NextSong"]["Artists"]
    assert obj.NextSong.Duration == media_fixture_response["NextSong"]["Duration"]
    assert (
        obj.NextSong.DeepLinks[0].Kind
        == media_fixture_response["NextSong"]["DeepLinks"][0]["Kind"]
    )
    assert (
        obj.NextSong.DeepLinks[0].Title
        == media_fixture_response["NextSong"]["DeepLinks"][0]["Title"]
    )
    assert (
        obj.NextSong.DeepLinks[0].Uri
        == media_fixture_response["NextSong"]["DeepLinks"][0]["Uri"]
    )
    assert (
        obj.NextSong.DeepLinks[0].MediaId
        == media_fixture_response["NextSong"]["DeepLinks"][0]["MediaId"]
    )
    assert obj.NextSong.BitRate == media_fixture_response["NextSong"]["BitRate"]
    assert (
        obj.NextSong.ListenerCount
        == media_fixture_response["NextSong"]["ListenerCount"]
    )
    assert obj.NextSong.Rating == media_fixture_response["NextSong"]["Rating"]
    assert obj.NextSong.TotalItems == media_fixture_response["NextSong"]["TotalItems"]
    assert (
        obj.NextSong.DisplayInfo[0]
        == media_fixture_response["NextSong"]["DisplayInfo"][0]
    )
    assert (
        obj.NextSong.ContextMenuItems[0].Type
        == media_fixture_response["NextSong"]["ContextMenuItems"][0]["Type"]
    )
    assert (
        obj.NextSong.ContextMenuItems[0].Key
        == media_fixture_response["NextSong"]["ContextMenuItems"][0]["Key"]
    )
    assert (
        obj.NextSong.ContextMenuItems[0].Title
        == media_fixture_response["NextSong"]["ContextMenuItems"][0]["Title"]
    )
    assert (
        obj.NextSong.ContextMenuItems[0].Value
        == media_fixture_response["NextSong"]["ContextMenuItems"][0]["Value"]
    )
    assert obj.CurrProgress == media_fixture_response["CurrProgress"]
    assert obj.SearchPromptText == media_fixture_response["SearchPromptText"]
    assert obj.SourceLockedByZoneID == media_fixture_response["SourceLockedByZoneID"]
    assert obj.ServiceName == media_fixture_response["ServiceName"]
    assert obj.ServiceID == media_fixture_response["ServiceID"]
    assert obj.ServiceLogoURI == media_fixture_response["ServiceLogoURI"]
