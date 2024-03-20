/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Student } from '../models/Student';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class StudentsService {
    /**
     * Get Students
     * @returns Student OK
     * @throws ApiError
     */
    public static getStudents(): CancelablePromise<Array<Student>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/students',
        });
    }
    /**
     * Get Student
     * @returns Student OK
     * @throws ApiError
     */
    public static getStudent({
        firstName,
    }: {
        firstName: string,
    }): CancelablePromise<Array<Student>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/students/{firstName}',
            path: {
                'firstName': firstName,
            },
        });
    }
    /**
     * Get Student School
     * @returns Student OK
     * @throws ApiError
     */
    public static getStudentSchool({
        firstName,
    }: {
        firstName: string,
    }): CancelablePromise<Array<Student>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/students/{firstName}/school',
            path: {
                'firstName': firstName,
            },
        });
    }
}
