/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { School } from '../models/School';
import type { Student } from '../models/Student';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class SchoolService {
    /**
     * Get Schools
     * @returns School OK
     * @throws ApiError
     */
    public static getSchools(): CancelablePromise<Array<School>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/schools',
        });
    }
    /**
     * Get School
     * @returns any OK
     * @throws ApiError
     */
    public static getSchool({
        name,
    }: {
        name: string,
    }): CancelablePromise<(School | null)> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/schools/{name}',
            path: {
                'name': name,
            },
        });
    }
    /**
     * Get School Student
     * @returns Student OK
     * @throws ApiError
     */
    public static getSchoolStudent({
        name,
    }: {
        name: string,
    }): CancelablePromise<Array<Student>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/schools/{name}/students',
            path: {
                'name': name,
            },
        });
    }
}
