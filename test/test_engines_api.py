# coding: utf-8

"""
    Engine api

    Engine APIs  # noqa: E501

    The version of the OpenAPI document: 1.0.4
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import vtpl_api
from vtpl_api.api.engines_api import EnginesApi  # noqa: E501
from vtpl_api.rest import ApiException


class TestEnginesApi(unittest.TestCase):
    """EnginesApi unit test stubs"""

    def setUp(self):
        self.api = vtpl_api.api.engines_api.EnginesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_anpr_events_get(self):
        """Test case for anpr_events_get

        Get all anprEvents  # noqa: E501
        """
        pass

    def test_anpr_events_id_get(self):
        """Test case for anpr_events_id_get

        Get anprEvent by id  # noqa: E501
        """
        pass

    def test_anpr_events_post(self):
        """Test case for anpr_events_post

        Create an anprEvent  # noqa: E501
        """
        pass

    def test_atccs_events_get(self):
        """Test case for atccs_events_get

        Get all Automatic Traffic Count Events  # noqa: E501
        """
        pass

    def test_atccs_events_id_get(self):
        """Test case for atccs_events_id_get

        Get Automatic Traffic Count Event by id  # noqa: E501
        """
        pass

    def test_atccs_events_post(self):
        """Test case for atccs_events_post

        Create an Automatic Traffic Count Event  # noqa: E501
        """
        pass

    def test_capabilities_get(self):
        """Test case for capabilities_get

        Get all capabilities of engines  # noqa: E501
        """
        pass

    def test_capabilities_post(self):
        """Test case for capabilities_post

        Create a capability  # noqa: E501
        """
        pass

    def test_central_face_database_get(self):
        """Test case for central_face_database_get

        Get Central Face Database address  # noqa: E501
        """
        pass

    def test_central_face_database_id_delete(self):
        """Test case for central_face_database_id_delete

        Delete central face database  # noqa: E501
        """
        pass

    def test_central_face_database_id_get(self):
        """Test case for central_face_database_id_get

        Get central face database by id  # noqa: E501
        """
        pass

    def test_central_face_database_id_patch(self):
        """Test case for central_face_database_id_patch

        Patch central face database  # noqa: E501
        """
        pass

    def test_central_face_database_post(self):
        """Test case for central_face_database_post

        Create a centralFaceDatabase address  # noqa: E501
        """
        pass

    def test_clips_get(self):
        """Test case for clips_get

        Get all unprocesed clips  # noqa: E501
        """
        pass

    def test_clips_id_get(self):
        """Test case for clips_id_get

        Get clip by id  # noqa: E501
        """
        pass

    def test_clips_post(self):
        """Test case for clips_post

        Create an unprocesed clip  # noqa: E501
        """
        pass

    def test_crowd_abnormality_events_get(self):
        """Test case for crowd_abnormality_events_get

        Get all crowdAbnormalityEvents  # noqa: E501
        """
        pass

    def test_crowd_abnormality_events_id_get(self):
        """Test case for crowd_abnormality_events_id_get

        Get crowdAbnormalityEvent by id  # noqa: E501
        """
        pass

    def test_crowd_abnormality_events_post(self):
        """Test case for crowd_abnormality_events_post

        Create a crowdAbnormalityEvent  # noqa: E501
        """
        pass

    def test_crowd_dispersion_events_get(self):
        """Test case for crowd_dispersion_events_get

        Get all crowdDispersionEvents  # noqa: E501
        """
        pass

    def test_crowd_dispersion_events_id_get(self):
        """Test case for crowd_dispersion_events_id_get

        Get crowdDispersionEvent by id  # noqa: E501
        """
        pass

    def test_crowd_dispersion_events_post(self):
        """Test case for crowd_dispersion_events_post

        Create a crowdDispersionEvent  # noqa: E501
        """
        pass

    def test_crowd_formation_events_get(self):
        """Test case for crowd_formation_events_get

        Get all crowdFormationEvents  # noqa: E501
        """
        pass

    def test_crowd_formation_events_id_get(self):
        """Test case for crowd_formation_events_id_get

        Get crowdFormationEvent by id  # noqa: E501
        """
        pass

    def test_crowd_formation_events_post(self):
        """Test case for crowd_formation_events_post

        Create a crowdFormationEvent  # noqa: E501
        """
        pass

    def test_driver_on_call_events_get(self):
        """Test case for driver_on_call_events_get

        Get all driverOnCallEvents  # noqa: E501
        """
        pass

    def test_driver_on_call_events_id_get(self):
        """Test case for driver_on_call_events_id_get

        Get driverOnCallEvent by id  # noqa: E501
        """
        pass

    def test_driver_on_call_events_post(self):
        """Test case for driver_on_call_events_post

        Create a driverOnCallEvent  # noqa: E501
        """
        pass

    def test_engine_tasks_get(self):
        """Test case for engine_tasks_get

        Get all engineTasks  # noqa: E501
        """
        pass

    def test_engine_tasks_id_delete(self):
        """Test case for engine_tasks_id_delete

        Delete an engine task  # noqa: E501
        """
        pass

    def test_engine_tasks_id_get(self):
        """Test case for engine_tasks_id_get

        Get engine task by id  # noqa: E501
        """
        pass

    def test_engine_tasks_id_patch(self):
        """Test case for engine_tasks_id_patch

        Patch an engine task  # noqa: E501
        """
        pass

    def test_engine_tasks_post(self):
        """Test case for engine_tasks_post

        Create an engineTask  # noqa: E501
        """
        pass

    def test_engines_get(self):
        """Test case for engines_get

        Get all engine details  # noqa: E501
        """
        pass

    def test_engines_id_delete(self):
        """Test case for engines_id_delete

        Delete an engine  # noqa: E501
        """
        pass

    def test_engines_id_get(self):
        """Test case for engines_id_get

        Get engine by id  # noqa: E501
        """
        pass

    def test_engines_post(self):
        """Test case for engines_post

        Create an engine  # noqa: E501
        """
        pass

    def test_event_snaps_get(self):
        """Test case for event_snaps_get

        Get all eventSnaps  # noqa: E501
        """
        pass

    def test_event_snaps_id_get(self):
        """Test case for event_snaps_id_get

        Get eventSnap by id  # noqa: E501
        """
        pass

    def test_event_snaps_post(self):
        """Test case for event_snaps_post

        Create an eventSnap  # noqa: E501
        """
        pass

    def test_face_events_get(self):
        """Test case for face_events_get

        Get all faceEvents  # noqa: E501
        """
        pass

    def test_face_events_id_get(self):
        """Test case for face_events_id_get

        Get faceEvent by id  # noqa: E501
        """
        pass

    def test_face_events_post(self):
        """Test case for face_events_post

        Create a faceEvent  # noqa: E501
        """
        pass

    def test_face_snaps_get(self):
        """Test case for face_snaps_get

        Get all faceSnaps  # noqa: E501
        """
        pass

    def test_face_snaps_post(self):
        """Test case for face_snaps_post

        Create a faceSnap  # noqa: E501
        """
        pass

    def test_fancy_lp_events_get(self):
        """Test case for fancy_lp_events_get

        Get all Fancy License Plate Events  # noqa: E501
        """
        pass

    def test_fancy_lp_events_id_get(self):
        """Test case for fancy_lp_events_id_get

        Get Fancy License Plate Event by id  # noqa: E501
        """
        pass

    def test_fancy_lp_events_post(self):
        """Test case for fancy_lp_events_post

        Create a Fancy License Plate Event  # noqa: E501
        """
        pass

    def test_intrusion_detection_cloud_events_get(self):
        """Test case for intrusion_detection_cloud_events_get

        Get all intrusionDetectionCloudEvents  # noqa: E501
        """
        pass

    def test_intrusion_detection_cloud_events_id_get(self):
        """Test case for intrusion_detection_cloud_events_id_get

        Get intrusionDetectionCloudEvent by id  # noqa: E501
        """
        pass

    def test_intrusion_detection_cloud_events_post(self):
        """Test case for intrusion_detection_cloud_events_post

        Create a intrusionDetectionCloudEvent  # noqa: E501
        """
        pass

    def test_intrusion_detection_edge_events_get(self):
        """Test case for intrusion_detection_edge_events_get

        Get all intrusionDetectionEdgeEvents  # noqa: E501
        """
        pass

    def test_intrusion_detection_edge_events_id_get(self):
        """Test case for intrusion_detection_edge_events_id_get

        Get intrusionDetectionEdgeEvent by id  # noqa: E501
        """
        pass

    def test_intrusion_detection_edge_events_post(self):
        """Test case for intrusion_detection_edge_events_post

        Create a intrusionDetectionEdgeEvent  # noqa: E501
        """
        pass

    def test_no_helmet_events_get(self):
        """Test case for no_helmet_events_get

        Get all No Helmet Events  # noqa: E501
        """
        pass

    def test_no_helmet_events_id_get(self):
        """Test case for no_helmet_events_id_get

        Get No Helmet Event by id  # noqa: E501
        """
        pass

    def test_no_helmet_events_post(self):
        """Test case for no_helmet_events_post

        Create an No Helmet Event  # noqa: E501
        """
        pass

    def test_no_lp_events_get(self):
        """Test case for no_lp_events_get

        Get all No License Plate Events  # noqa: E501
        """
        pass

    def test_no_lp_events_id_get(self):
        """Test case for no_lp_events_id_get

        Get No License Plate Event by id  # noqa: E501
        """
        pass

    def test_no_lp_events_post(self):
        """Test case for no_lp_events_post

        Create a No License Plate Event  # noqa: E501
        """
        pass

    def test_no_seat_belt_events_get(self):
        """Test case for no_seat_belt_events_get

        Get all noSeatBeltEvents  # noqa: E501
        """
        pass

    def test_no_seat_belt_events_id_get(self):
        """Test case for no_seat_belt_events_id_get

        Get noSeatBeltEvent by id  # noqa: E501
        """
        pass

    def test_no_seat_belt_events_post(self):
        """Test case for no_seat_belt_events_post

        Create a noSeatBeltEvent  # noqa: E501
        """
        pass

    def test_people_collapsing_events_get(self):
        """Test case for people_collapsing_events_get

        Get all peopleCollapsingEvents  # noqa: E501
        """
        pass

    def test_people_collapsing_events_id_get(self):
        """Test case for people_collapsing_events_id_get

        Get peopleCollapsingEvent by id  # noqa: E501
        """
        pass

    def test_people_collapsing_events_post(self):
        """Test case for people_collapsing_events_post

        Create a peopleCollapsingEvent  # noqa: E501
        """
        pass

    def test_people_detail_events_get(self):
        """Test case for people_detail_events_get

        Get all peopleDetailEvents  # noqa: E501
        """
        pass

    def test_people_detail_events_id_get(self):
        """Test case for people_detail_events_id_get

        Get peopleDetailEvent by id  # noqa: E501
        """
        pass

    def test_people_detail_events_post(self):
        """Test case for people_detail_events_post

        Create a peopleDetailEvent  # noqa: E501
        """
        pass

    def test_people_on_road_events_get(self):
        """Test case for people_on_road_events_get

        Get all People On Road Events  # noqa: E501
        """
        pass

    def test_people_on_road_events_id_get(self):
        """Test case for people_on_road_events_id_get

        Get People On Road Event by id  # noqa: E501
        """
        pass

    def test_people_on_road_events_post(self):
        """Test case for people_on_road_events_post

        Create a People On Road Event  # noqa: E501
        """
        pass

    def test_registered_faces_get(self):
        """Test case for registered_faces_get

        Get Registered Faces  # noqa: E501
        """
        pass

    def test_registered_faces_id_delete(self):
        """Test case for registered_faces_id_delete

        Delete a Registered Face  # noqa: E501
        """
        pass

    def test_registered_faces_id_get(self):
        """Test case for registered_faces_id_get

        Get Registered Face  # noqa: E501
        """
        pass

    def test_registered_faces_id_patch(self):
        """Test case for registered_faces_id_patch

        Patch a Registered Face  # noqa: E501
        """
        pass

    def test_registered_faces_post(self):
        """Test case for registered_faces_post

        Create a Registered Face  # noqa: E501
        """
        pass

    def test_snaps_get(self):
        """Test case for snaps_get

        Get all unprocesed snaps  # noqa: E501
        """
        pass

    def test_snaps_id_get(self):
        """Test case for snaps_id_get

        Get snap by id  # noqa: E501
        """
        pass

    def test_snaps_post(self):
        """Test case for snaps_post

        Create a unprocesed snap  # noqa: E501
        """
        pass

    def test_sub_systems_get(self):
        """Test case for sub_systems_get

        Get all Sub System details  # noqa: E501
        """
        pass

    def test_sub_systems_id_delete(self):
        """Test case for sub_systems_id_delete

        Delete a Sub System  # noqa: E501
        """
        pass

    def test_sub_systems_id_get(self):
        """Test case for sub_systems_id_get

        Get Sub System by id  # noqa: E501
        """
        pass

    def test_sub_systems_id_patch(self):
        """Test case for sub_systems_id_patch

        Patch a Sub System  # noqa: E501
        """
        pass

    def test_sub_systems_post(self):
        """Test case for sub_systems_post

        Create a Sub System  # noqa: E501
        """
        pass

    def test_vehicle_congestion_events_get(self):
        """Test case for vehicle_congestion_events_get

        Get all Vehicle Congestion Events  # noqa: E501
        """
        pass

    def test_vehicle_congestion_events_id_get(self):
        """Test case for vehicle_congestion_events_id_get

        Get Vehicle Congestion Event by id  # noqa: E501
        """
        pass

    def test_vehicle_congestion_events_post(self):
        """Test case for vehicle_congestion_events_post

        Create a Vehicle Congestion Event  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
