import { beforeEach, describe, expect, test, vi } from 'vitest'
import { createUser, fetchUsers } from './users.service'
import axios from "axios"

vi.mock(axios)

