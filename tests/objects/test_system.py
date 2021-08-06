"""
Generated by generator/generator.py - 2021-07-31 12:29:43.406741
"""
from pycasatunes.objects.system import CasaTunesSystem
from tests.responses.system_fixture import system_fixture_response


def test_system(system_fixture_response):
    obj = CasaTunesSystem(system_fixture_response)
    assert obj.AppName == system_fixture_response["AppName"]
    assert obj.ControllerFeatures == system_fixture_response["ControllerFeatures"]
    assert obj.EQSettings.Minimum == system_fixture_response["EQSettings"]["Minimum"]
    assert obj.EQSettings.Maximum == system_fixture_response["EQSettings"]["Maximum"]
    assert (
        obj.EQSettings.Increment == system_fixture_response["EQSettings"]["Increment"]
    )
    assert (
        obj.VolumeSettings.Minimum
        == system_fixture_response["VolumeSettings"]["Minimum"]
    )
    assert (
        obj.VolumeSettings.Maximum
        == system_fixture_response["VolumeSettings"]["Maximum"]
    )
    assert (
        obj.VolumeSettings.Increment
        == system_fixture_response["VolumeSettings"]["Increment"]
    )
    assert obj.MACAddress == system_fixture_response["MACAddress"]
    assert obj.TeamViewerMACAddress == system_fixture_response["TeamViewerMACAddress"]
    assert obj.IPAddress == system_fixture_response["IPAddress"]
    assert obj.CasaTunesVersion == system_fixture_response["CasaTunesVersion"]
    assert obj.WebServicesVersion == system_fixture_response["WebServicesVersion"]
    assert obj.RESTServicesVersion == system_fixture_response["RESTServicesVersion"]
    assert obj.IsLicenseValid == system_fixture_response["IsLicenseValid"]
    assert obj.IsCAMSupported == system_fixture_response["IsCAMSupported"]
    assert obj.IsAirableLicensed == system_fixture_response["IsAirableLicensed"]
    assert obj.IsSystemSleepEnabled == system_fixture_response["IsSystemSleepEnabled"]
    assert obj.IsPasswordRequired == system_fixture_response["IsPasswordRequired"]
    assert obj.StreamerModeEnabled == system_fixture_response["StreamerModeEnabled"]
    assert (
        obj.IsSettingsPasswordRequired
        == system_fixture_response["IsSettingsPasswordRequired"]
    )
    assert obj.IsPrayersEnabled == system_fixture_response["IsPrayersEnabled"]
    assert obj.IndexerPort == system_fixture_response["IndexerPort"]
    assert obj.MatrixInfo[0].Title == system_fixture_response["MatrixInfo"][0]["Title"]
    assert (
        obj.MatrixInfo[0].Values == system_fixture_response["MatrixInfo"][0]["Values"]
    )